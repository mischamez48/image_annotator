"""
Setup file for the DigitalSreeni Image Annotator package.
Simplified version for easy installation.

@DigitalSreeni
Dr. Sreenivas Bhattiprolu
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="digitalsreeni-image-annotator-enhanced",
    version="0.8.12",
    author="Dr. Sreenivas Bhattiprolu (Original), Enhanced by Community",
    author_email="digitalsreeni@gmail.com",
    description="Enhanced version of DigitalSreeni Image Annotator with additional SAM-2 prompt modalities and improved functionality",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bnsreenu/digitalsreeni-image-annotator",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "PyQt5>=5.15.0",
        "numpy>=1.24.0",
        "Pillow>=10.0.0",
        "tifffile>=2023.1.0",
        "czifile>=2019.7.0",
        "opencv-python>=4.8.0",
        "pyyaml>=6.0",
        "scikit-image>=0.21.0",
        "ultralytics>=8.0.0",
        "plotly>=5.15.0",
        "shapely>=2.0.0", 
        "pystackreg>=0.2.0",
        "pydicom>=2.4.0"
    ],
    entry_points={
        "console_scripts": [
            "digitalsreeni-image-annotator=digitalsreeni_image_annotator.main:main",
            "sreeni=digitalsreeni_image_annotator.main:main", 
        ],
    },
)
