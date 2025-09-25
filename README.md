# DigitalSreeni Image Annotator - Enhanced Version

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![Version](https://img.shields.io/badge/version-0.8.12-orange)
![Based On](https://img.shields.io/badge/based%20on-DigitalSreeni%20Image%20Annotator-blue)

A powerful and user-friendly tool for annotating images with polygons, rectangles, and advanced SAM-2 assisted annotations. This enhanced version is **based on the original work by Dr. Sreenivas Bhattiprolu (@DigitalSreeni)** with additional functionalities including multiple prompt modalities (Points, Bounding Boxes, Masks) and improved merging capabilities.

> **Note**: This is an enhanced fork of the original [DigitalSreeni Image Annotator](https://github.com/bnsreenu/digitalsreeni-image-annotator) by Dr. Sreenivas Bhattiprolu. All original functionality is preserved with additional features added on top.

## ✨ Enhanced Features (Added to Original)

- **Multiple SAM-2 Prompt Modalities**: Points, Bounding Boxes, and Masks
- **Enhanced Merge Functionality**: Properly merges different annotation types (rectangles with polygons)
- **Improved User Experience**: Better keyboard shortcuts and visual feedback
- **Easy Installation**: One-click setup scripts for different platforms

## 🎯 Original Features (by Dr. Sreenivas Bhattiprolu)

- **Semi-automated annotations** with SAM-2 assistance (Segment Anything Model)
- **Manual annotations** with polygons and rectangles
- **Paint brush and Eraser tools** with adjustable pen sizes
- **Save and load projects** for continued work
- **Import/Export** in multiple formats (COCO JSON, YOLO v8/v11, Labeled images, etc.)
- **Multi-dimensional image support** (TIFF stacks and CZI files)
- **Zoom and pan** for detailed annotations
- **Multiple classes** with customizable colors
- **Dark mode** support
- **YOLO training** capabilities
- **Area measurements** for annotations
- **Additional tools**: Dataset splitter, image augmenter, DICOM converter, and more
- **Real-time SAM-2 Integration**: Automatic model downloading and inference

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Windows, macOS, or Linux

### Installation

#### Option 1: Clone from GitHub (Recommended)
```bash
git clone https://github.com/yourusername/digitalsreeni-image-annotator.git
cd digitalsreeni-image-annotator
```

#### Option 2: Download ZIP
1. Download the project as a ZIP file
2. Extract to your desired location

### Setup

**Method A: Automatic Installation (Windows)**
```bash
# Double-click install.bat or run in command prompt
install.bat
```

**Method B: PowerShell Installation (Windows)**
```bash
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\install.ps1
```

**Method C: Manual Installation (All Platforms)**
```bash
# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

**Method D: Using pip directly**
```bash
pip install git+https://github.com/yourusername/digitalsreeni-image-annotator.git
```

### Running the Application

**Option 1: Using the launcher script**
```bash
python run_annotator.py
```

**Option 2: Using the installed command**
```bash
digitalsreeni-image-annotator
```

**Option 3: Direct module execution**
```bash
python -m src.digitalsreeni_image_annotator.main
```

## 🎯 Features

### 🎯 Core Annotation Tools (Original)
- **Manual annotations** with polygons and rectangles
- **Paint brush and Eraser tools** with adjustable pen sizes
- **Multi-class support** with customizable colors
- **Zoom and pan** for detailed annotations
- **Area measurements** for annotations

### 🤖 SAM-2 Assisted Annotations (Enhanced)
- **Multiple Prompt Modalities** (Enhanced):
  - **Points**: Left-click for positive points, right-click for negative points
  - **Bounding Boxes**: Click and drag to draw rectangles
  - **Masks**: Click and drag to draw custom shapes
- **Real-time prediction** with visual feedback
- **Model selection**: Choose from SAM-2 tiny, small, base, or large
- **Automatic model downloading** on first use

### 🔧 Advanced Features
- **Enhanced Merge Functionality** (Enhanced): Properly merges different annotation types
- **Save and load projects** for continued work
- **Import/Export** in multiple formats (COCO JSON, YOLO v8/v11, Labeled images, etc.)
- **Multi-dimensional image support** (TIFF stacks and CZI files)
- **Dark mode** support
- **YOLO training** capabilities
- **Additional tools**: Dataset splitter, image augmenter, DICOM converter, and more

### ⌨️ Keyboard Shortcuts
- **Enter**: Accept current SAM prediction
- **Esc**: Clear current prompts
- **C**: Clear points (Points modality)
- **Ctrl+N**: New project
- **Ctrl+O**: Open project
- **Ctrl+S**: Save project
- **F1**: Help

## 📁 Project Structure

```
digitalsreeni-image-annotator/
├── src/
│   └── digitalsreeni_image_annotator/    # Main application code
│       ├── annotator_window.py          # Main GUI window
│       ├── image_label.py               # Image display and interaction
│       ├── sam_utils.py                 # SAM-2 integration
│       ├── export_formats.py            # Export functionality
│       ├── import_formats.py            # Import functionality
│       ├── yolo_trainer.py              # YOLO training
│       └── ...                          # Additional modules
├── data/                                # Sample data and projects
│   ├── project1/                        # Example project
│   └── YOLO11n-model-yaml/              # YOLO configuration
├── screenshots/                         # Application screenshots
├── requirements.txt                     # Python dependencies
├── setup.py                            # Package setup
├── run_annotator.py                    # Simple launcher script
├── test_installation.py                # Installation test
├── LICENSE                              # MIT License
└── README.md                           # This file
```

## 🛠️ Usage

### Basic Workflow

1. **Start a new project**: Click "New Project" or use Ctrl+N
2. **Add images**: Use "Add New Images" to import images, including TIFF stacks and CZI files
3. **Add classes**: Use the "Add Classes" button to define annotation classes
4. **Annotate**: 
   - Select a class and use Polygon, Rectangle, or Paint Brush tools for manual annotation
   - Use SAM2-assisted annotation for semi-automated labeling
   - Adjust pen/eraser size with - and = keys
5. **Save your work**: Use "Save Project" or Ctrl+S

### SAM-2 Assisted Annotation

1. **Select a SAM Model**: Choose from the dropdown (SAM 2 tiny, small, base, or large)
2. **Choose Prompt Type**: Select from "Bounding Box", "Points", or "Mask" dropdown
3. **Activate SAM-Assisted**: Click the "SAM-Assisted" button
4. **Create Prompts**:
   - **Bounding Box**: Click and drag to draw a rectangle
   - **Points**: Left-click for positive points, right-click for negative points
   - **Mask**: Click and drag to draw a mask/polygon
5. **Apply**: The SAM-2 model will automatically generate segmentation based on your prompt

### Merging Annotations

1. **Select multiple annotations** from the annotation list
2. **Click "Merge"** button
3. **Choose whether to keep** original annotations
4. **Result**: All selected annotations are combined into a single polygon

## 🔧 Development

### Running Tests
```bash
python test_installation.py
```

### Building from Source
```bash
git clone https://github.com/yourusername/digitalsreeni-image-annotator.git
cd digitalsreeni-image-annotator
pip install -e .
```

## 📋 Requirements

### Core Dependencies
- PyQt5>=5.15.0
- numpy>=1.24.0
- Pillow>=10.0.0
- opencv-python>=4.8.0
- scikit-image>=0.21.0

### File Format Support
- tifffile>=2023.1.0
- czifile>=2019.7.0
- pydicom>=2.4.0

### Machine Learning
- ultralytics>=8.0.0 (for SAM-2 and YOLO)

### Additional Libraries
- pyyaml>=6.0
- shapely>=2.0.0
- plotly>=5.15.0
- pystackreg>=0.2.0

## 🐛 Troubleshooting

### Common Issues

1. **Import errors**: Make sure all dependencies are installed:
   ```bash
   pip install -r requirements.txt
   ```

2. **PyQt5 issues on Linux**: If you encounter XCB plugin errors:
   ```bash
   sudo apt-get install python3-pyqt5
   ```

3. **SAM2 model download**: First-time SAM2 usage requires internet connection to download models

4. **Memory issues**: For large images, consider using smaller SAM2 models (tiny or small)

### Getting Help

- Check the built-in help (F1 key)
- Visit the original project: https://github.com/bnsreenu/digitalsreeni-image-annotator
- Watch tutorial videos on the DigitalSreeni YouTube channel

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Original Author**: Dr. Sreenivas Bhattiprolu (@DigitalSreeni)
- **Original Repository**: https://github.com/bnsreenu/digitalsreeni-image-annotator
- **Enhanced Features**: Multiple prompt modalities and improved merging functionality added to the original work

### Credits
This enhanced version is built upon the excellent foundation provided by Dr. Sreenivas Bhattiprolu's original DigitalSreeni Image Annotator. All original functionality has been preserved, and additional features have been added to enhance the user experience and capabilities.

## 📞 Contact

Dr. Sreenivas Bhattiprolu - [@DigitalSreeni](https://twitter.com/DigitalSreeni)

## 🔗 Links

- [Original Project](https://github.com/bnsreenu/digitalsreeni-image-annotator)
- [YouTube Channel](http://www.youtube.com/c/DigitalSreeni)
- [PayPal Donation](https://www.paypal.com/donate/?business=FGQL3CNJGJP9C)

## 📊 Citing

If you use this software in your research, please cite it as follows:

```bibtex
@software{digitalsreeni_image_annotator,
  author = {Bhattiprolu, Sreenivas},
  title = {DigitalSreeni Image Annotator},
  year = {2024},
  url = {https://github.com/bnsreenu/digitalsreeni-image-annotator}
}
```

---

## 📋 Attribution

This enhanced version is based on the original **DigitalSreeni Image Annotator** by Dr. Sreenivas Bhattiprolu (@DigitalSreeni). 

- **Original Repository**: https://github.com/bnsreenu/digitalsreeni-image-annotator
- **Original Author**: Dr. Sreenivas Bhattiprolu
- **Enhanced Features**: Multiple SAM-2 prompt modalities, improved merging, and better user experience

**Note**: This is an enhanced version of the original DigitalSreeni Image Annotator with additional features for improved usability and functionality. All original functionality is preserved and enhanced.
