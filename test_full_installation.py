#!/usr/bin/env python3
"""
Comprehensive test script for the DigitalSreeni Image Annotator.
This script tests all major components and features.

@DigitalSreeni
Dr. Sreenivas Bhattiprolu
"""

import sys
import os
import traceback

def test_imports():
    """Test if all required modules can be imported."""
    print("Testing imports...")
    
    try:
        # Core dependencies
        import PyQt5
        print("✓ PyQt5")
        
        import numpy
        print("✓ numpy")
        
        import PIL
        print("✓ PIL (Pillow)")
        
        import cv2
        print("✓ opencv-python")
        
        import tifffile
        print("✓ tifffile")
        
        import czifile
        print("✓ czifile")
        
        import yaml
        print("✓ pyyaml")
        
        import skimage
        print("✓ scikit-image")
        
        import ultralytics
        print("✓ ultralytics")
        
        import plotly
        print("✓ plotly")
        
        import shapely
        print("✓ shapely")
        
        import pystackreg
        print("✓ pystackreg")
        
        import pydicom
        print("✓ pydicom")
        
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_application_components():
    """Test if the main application components can be created."""
    print("\nTesting application components...")
    
    try:
        # Add src to path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        src_dir = os.path.join(current_dir, 'src')
        sys.path.insert(0, src_dir)
        
        # Test main modules
        from digitalsreeni_image_annotator.main import main
        print("✓ Main module")
        
        from digitalsreeni_image_annotator.annotator_window import ImageAnnotator
        print("✓ Annotator window")
        
        from digitalsreeni_image_annotator.image_label import ImageLabel
        print("✓ Image label")
        
        from digitalsreeni_image_annotator.sam_utils import SAMUtils
        print("✓ SAM utilities")
        
        from digitalsreeni_image_annotator.utils import calculate_area, calculate_bbox
        print("✓ Utility functions")
        
        return True
        
    except Exception as e:
        print(f"✗ Component error: {e}")
        traceback.print_exc()
        return False

def test_ui_creation():
    """Test if the UI can be created without errors."""
    print("\nTesting UI creation...")
    
    try:
        from PyQt5.QtWidgets import QApplication
        from digitalsreeni_image_annotator.annotator_window import ImageAnnotator
        
        # Create QApplication (required for PyQt5)
        app = QApplication(sys.argv)
        
        # Create main window
        window = ImageAnnotator()
        
        # Test key components
        assert hasattr(window, 'image_label'), "Missing image_label"
        assert hasattr(window, 'sam_utils'), "Missing sam_utils"
        assert hasattr(window, 'prompt_modality_selector'), "Missing prompt_modality_selector"
        assert hasattr(window, 'sam_model_selector'), "Missing sam_model_selector"
        
        print("✓ UI components created successfully")
        
        # Test prompt modalities
        modalities = ["Bounding Box", "Points", "Mask"]
        for modality in modalities:
            window.image_label.set_prompt_modality(modality)
            assert window.image_label.prompt_modality == modality, f"Failed to set modality: {modality}"
        
        print("✓ Prompt modalities working")
        
        # Test SAM model selector
        sam_models = list(window.sam_utils.sam_models.keys())
        assert len(sam_models) > 0, "No SAM models available"
        print(f"✓ SAM models available: {sam_models}")
        
        app.quit()
        return True
        
    except Exception as e:
        print(f"✗ UI creation error: {e}")
        traceback.print_exc()
        return False

def test_annotation_utilities():
    """Test annotation utility functions."""
    print("\nTesting annotation utilities...")
    
    try:
        from PyQt5.QtWidgets import QApplication
        from digitalsreeni_image_annotator.annotator_window import ImageAnnotator
        
        # Create a test instance
        app = QApplication(sys.argv)
        window = ImageAnnotator()
        
        # Test annotation to polygon conversion
        test_annotation_polygon = {
            "segmentation": [0, 0, 100, 0, 100, 100, 0, 100],
            "category_name": "test"
        }
        
        test_annotation_bbox = {
            "bbox": [0, 0, 100, 100],
            "category_name": "test"
        }
        
        # Test polygon conversion
        poly1 = window.annotation_to_polygon(test_annotation_polygon)
        assert poly1 is not None, "Failed to convert polygon annotation"
        
        # Test bbox conversion
        poly2 = window.annotation_to_polygon(test_annotation_bbox)
        assert poly2 is not None, "Failed to convert bbox annotation"
        
        print("✓ Annotation conversion utilities working")
        
        app.quit()
        return True
        
    except Exception as e:
        print(f"✗ Annotation utilities error: {e}")
        traceback.print_exc()
        return False

def main():
    """Run all tests."""
    print("DigitalSreeni Image Annotator - Installation Test")
    print("=" * 50)
    
    tests = [
        ("Dependencies", test_imports),
        ("Application Components", test_application_components),
        ("UI Creation", test_ui_creation),
        ("Annotation Utilities", test_annotation_utilities)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n{test_name}:")
        try:
            if test_func():
                passed += 1
                print(f"✓ {test_name} PASSED")
            else:
                print(f"✗ {test_name} FAILED")
        except Exception as e:
            print(f"✗ {test_name} FAILED with exception: {e}")
    
    print("\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The application is ready to use.")
        print("\nYou can now run the application using:")
        print("  python run_annotator.py")
        return True
    else:
        print("❌ Some tests failed. Please check the error messages above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)