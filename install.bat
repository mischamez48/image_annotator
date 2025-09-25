@echo off
echo DigitalSreeni Image Annotator - Installation Script
echo ==================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo Python found. Installing dependencies...
echo.

REM Install the package in development mode
pip install -e .

if errorlevel 1 (
    echo.
    echo ERROR: Installation failed. Trying with --user flag...
    pip install -e . --user
    if errorlevel 1 (
        echo.
        echo ERROR: Installation failed completely.
        echo Please check your Python environment and try again.
        pause
        exit /b 1
    )
)

echo.
echo Installation complete!
echo.
echo You can now run the application using:
echo   python run_annotator.py
echo   or
echo   digitalsreeni-image-annotator
echo.
echo To test the installation, run:
echo   python test_installation.py
echo.
pause
