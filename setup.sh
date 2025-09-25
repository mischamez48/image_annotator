#!/bin/bash
# DigitalSreeni Image Annotator - Linux/macOS Setup Script

echo "DigitalSreeni Image Annotator - Setup Script"
echo "============================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

# Check Python version
python_version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python $python_version is too old. Please install Python 3.8+ first."
    exit 1
fi

echo "✓ Python $python_version found"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip first."
    exit 1
fi

echo "✓ pip3 found"

# Install dependencies
echo "Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Install package in development mode
echo "Installing package in development mode..."
pip3 install -e .

if [ $? -eq 0 ]; then
    echo "✓ Package installed successfully"
else
    echo "❌ Failed to install package"
    exit 1
fi

# Run tests
echo "Running installation tests..."
python3 test_full_installation.py

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 Installation completed successfully!"
    echo ""
    echo "You can now run the application using:"
    echo "  python3 run_annotator.py"
    echo "  or"
    echo "  digitalsreeni-image-annotator"
else
    echo "❌ Installation tests failed. Please check the error messages above."
    exit 1
fi