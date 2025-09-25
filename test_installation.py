#!/usr/bin/env python3
"""
Test script to verify the DigitalSreeni Image Annotator installation.
This script checks if all required dependencies are available.

@DigitalSreeni
Dr. Sreenivas Bhattiprolu
"""

import sys
import importlib

def test_import(module_name, package_name=None):
    """Test if a module can be imported."""
    try:
        if package_name:
            importlib.import_module(module_name, package_name)
        else:
            importlib.import_module(module_name)
        print(f"✓ {module_name}")
        return True
    except ImportError as e:
        print(f"✗ {module_name} - {e}")
        return False

def main():
    """Test all required dependencies."""
    print("Testing DigitalSreeni Image Annotator Dependencies")
    print("=" * 50)
    
    # Core dependencies
    dependencies = [
        "PyQt5",
        "numpy", 
        "PIL",  # Pillow
        "cv2",  # opencv-python
        "tifffile",
        "czifile",
        "yaml",  # pyyaml
        "skimage",  # scikit-image
        "ultralytics",
        "plotly",
        "shapely",
        "pystackreg",
        "pydicom"
    ]
    
    success_count = 0
    total_count = len(dependencies)
    
    for dep in dependencies:
        if test_import(dep):
            success_count += 1
    
    print("\n" + "=" * 50)
    print(f"Installation Test Results: {success_count}/{total_count} dependencies available")
    
    if success_count == total_count:
        print("✓ All dependencies are installed correctly!")
        print("\nYou can now run the application using:")
        print("  python run_annotator.py")
        return True
    else:
        print("✗ Some dependencies are missing.")
        print("\nPlease install missing dependencies using:")
        print("  pip install -r requirements.txt")
        return False

if __name__ == "__main__":
    success = main()
    input("\nPress Enter to exit...")
    sys.exit(0 if success else 1)
