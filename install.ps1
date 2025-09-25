# DigitalSreeni Image Annotator Installation Script for PowerShell
# Run this script in PowerShell as Administrator if needed

Write-Host "DigitalSreeni Image Annotator - Installation Script" -ForegroundColor Green
Write-Host "==================================================" -ForegroundColor Green
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Found Python: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.8+ from https://python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "Installing dependencies..." -ForegroundColor Yellow
Write-Host ""

# Install dependencies
try {
    pip install -r requirements.txt
    Write-Host "Dependencies installed successfully!" -ForegroundColor Green
} catch {
    Write-Host "Error installing dependencies. Trying with --user flag..." -ForegroundColor Yellow
    pip install -r requirements.txt --user
}

Write-Host ""
Write-Host "Installing the package in development mode..." -ForegroundColor Yellow

try {
    pip install -e .
    Write-Host "Package installed successfully!" -ForegroundColor Green
} catch {
    Write-Host "Error installing package. Trying with --user flag..." -ForegroundColor Yellow
    pip install -e . --user
}

Write-Host ""
Write-Host "Installation complete!" -ForegroundColor Green
Write-Host ""
Write-Host "You can now run the application using:" -ForegroundColor Cyan
Write-Host "  python run_annotator.py" -ForegroundColor White
Write-Host "  or" -ForegroundColor White
Write-Host "  digitalsreeni-image-annotator" -ForegroundColor White
Write-Host ""
Write-Host "To test the installation, run:" -ForegroundColor Cyan
Write-Host "  python test_installation.py" -ForegroundColor White
Write-Host ""

Read-Host "Press Enter to exit"
