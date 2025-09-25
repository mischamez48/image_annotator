import numpy as np
import cv2
from PyQt5.QtGui import QImage, QColor
from ultralytics import SAM

class SAMUtils:
    def __init__(self):
        self.sam_models = {
            "SAM 2 tiny": "sam2_t.pt",
            "SAM 2 small": "sam2_s.pt",
            "SAM 2 base": "sam2_b.pt",
            "SAM 2 large": "sam2_l.pt"
        }
        self.current_sam_model = None
        self.sam_model = None

    def change_sam_model(self, model_name):
        if model_name != "Pick a SAM Model":
            self.current_sam_model = model_name
            self.sam_model = SAM(self.sam_models[self.current_sam_model])
            print(f"Changed SAM model to: {model_name}")
        else:
            self.current_sam_model = None
            self.sam_model = None
            print("SAM model unset")

    def qimage_to_numpy(self, qimage):
        width = qimage.width()
        height = qimage.height()
        fmt = qimage.format()

        if fmt == QImage.Format_Grayscale16:
            buffer = qimage.constBits().asarray(height * width * 2)
            image = np.frombuffer(buffer, dtype=np.uint16).reshape((height, width))
            image_8bit = self.normalize_16bit_to_8bit(image)
            return np.stack((image_8bit,) * 3, axis=-1)
        
        elif fmt == QImage.Format_RGB16:
            buffer = qimage.constBits().asarray(height * width * 2)
            image = np.frombuffer(buffer, dtype=np.uint16).reshape((height, width))
            image_8bit = self.normalize_16bit_to_8bit(image)
            return np.stack((image_8bit,) * 3, axis=-1)

        elif fmt == QImage.Format_Grayscale8:
            buffer = qimage.constBits().asarray(height * width)
            image = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width))
            return np.stack((image,) * 3, axis=-1)
        
        elif fmt in [QImage.Format_RGB32, QImage.Format_ARGB32, QImage.Format_ARGB32_Premultiplied]:
            buffer = qimage.constBits().asarray(height * width * 4)
            image = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width, 4))
            return image[:, :, :3]
        
        elif fmt == QImage.Format_RGB888:
            buffer = qimage.constBits().asarray(height * width * 3)
            image = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width, 3))
            return image
        
        elif fmt == QImage.Format_Indexed8:
            buffer = qimage.constBits().asarray(height * width)
            image = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width))
            color_table = qimage.colorTable()
            rgb_image = np.zeros((height, width, 3), dtype=np.uint8)
            for y in range(height):
                for x in range(width):
                    rgb_image[y, x] = QColor(color_table[image[y, x]]).getRgb()[:3]
            return rgb_image
        
        else:
            converted_image = qimage.convertToFormat(QImage.Format_RGB32)
            buffer = converted_image.constBits().asarray(height * width * 4)
            image = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width, 4))
            return image[:, :, :3]

    def normalize_16bit_to_8bit(self, array):
        return ((array - array.min()) / (array.max() - array.min()) * 255).astype(np.uint8)
    
    def mask_to_points(self, mask):
        """Convert a mask to points for SAM prompting."""
        try:
            # Find contours in the mask
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            if not contours:
                return []
            
            # Get the largest contour
            largest_contour = max(contours, key=cv2.contourArea)
            
            # Sample points along the contour
            points = []
            num_points = min(20, len(largest_contour))  # Limit to 20 points max
            step = len(largest_contour) // num_points
            
            for i in range(0, len(largest_contour), step):
                point = largest_contour[i][0]
                points.append((float(point[0]), float(point[1]), 1))  # Positive points
            
            # Add some interior points if the mask is large enough
            if len(points) > 0:
                # Find the centroid
                M = cv2.moments(largest_contour)
                if M["m00"] != 0:
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    points.append((float(cx), float(cy), 1))  # Center point
            
            return points
            
        except Exception as e:
            print(f"Error converting mask to points: {e}")
            return []

    def apply_sam_prediction(self, image, prompt_type, **kwargs):
        try:
            image_np = self.qimage_to_numpy(image)
            
            if prompt_type == "Bounding Box":
                bbox = kwargs.get('bbox')
                if bbox is None:
                    return None
                results = self.sam_model(image_np, bboxes=[bbox])
            elif prompt_type == "Points":
                points = kwargs.get('points', [])
                if not points:
                    return None
                # Convert points to the format expected by SAM
                point_coords = [[p[0], p[1]] for p in points]  # Convert to list of lists
                point_labels = [p[2] for p in points]
                results = self.sam_model(image_np, points=point_coords, labels=point_labels)
            elif prompt_type == "Mask":
                mask = kwargs.get('mask')
                if mask is None:
                    return None
                # Convert mask to points for SAM
                points = self.mask_to_points(mask)
                if not points:
                    return None
                point_coords = [[p[0], p[1]] for p in points]
                point_labels = [p[2] for p in points]
                results = self.sam_model(image_np, points=point_coords, labels=point_labels)
            else:
                print(f"Unknown prompt type: {prompt_type}")
                return None
            
            if results and len(results) > 0 and hasattr(results[0], 'masks') and results[0].masks is not None:
                mask = results[0].masks.data[0].cpu().numpy()
                
                if mask is not None:
                    print(f"Mask shape: {mask.shape}, Mask sum: {mask.sum()}")
                    contours = self.mask_to_polygon(mask)
                    print(f"Contours generated: {len(contours)} contour(s)")

                    if not contours:
                        print("No valid contours found")
                        return None

                    prediction = {
                        "segmentation": contours[0],
                        "score": float(results[0].boxes.conf[0]) if hasattr(results[0], 'boxes') and results[0].boxes is not None else 1.0
                    }
                    return prediction
                else:
                    print("Failed to generate mask")
                    return None
            else:
                print("No results from SAM model")
                return None
        except Exception as e:
            print(f"Error in applying SAM prediction: {str(e)}")
            import traceback
            traceback.print_exc()
            return None

    def mask_to_polygon(self, mask):
        import cv2
        contours, _ = cv2.findContours((mask > 0).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        polygons = []
        for contour in contours:
            if cv2.contourArea(contour) > 10:
                polygon = contour.flatten().tolist()
                if len(polygon) >= 6:
                    polygons.append(polygon)
        print(f"Generated {len(polygons)} valid polygons")
        return polygons