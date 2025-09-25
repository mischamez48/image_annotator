#!/usr/bin/env python3
"""
Simple launcher script for the DigitalSreeni Image Annotator.
This script ensures the application can be run easily without complex setup.

@DigitalSreeni
Dr. Sreenivas Bhattiprolu
"""

import sys
import os

# Add the src directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)

try:
    from digitalsreeni_image_annotator.main import main
    if __name__ == "__main__":
        main()
except ImportError as e:
    print(f"Error importing the application: {e}")
    print("\nPlease make sure all dependencies are installed by running:")
    print("  pip install -r requirements.txt")
    print("\nOr run the install.bat script for automatic installation.")
    input("\nPress Enter to exit...")
    sys.exit(1)
except Exception as e:
    print(f"Error running the application: {e}")
    input("\nPress Enter to exit...")
    sys.exit(1)
