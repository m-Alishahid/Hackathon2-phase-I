# PowerShell script to run the Todo Python Console App
# This provides Windows users with an easy way to run the application

param(
    [switch]$Help
)

if ($Help) {
    Write-Host "Todo App Runner (PowerShell)"
    Write-Host "Usage: .\run.ps1 [-Help]"
    Write-Host ""
    Write-Host "This script checks for Python and runs the Todo application."
    Write-Host "Requires Python 3.13+ to be installed and in PATH."
    exit 0
}

# Check if Python is available
try {
    $pythonVersion = python --version 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw "Python not found"
    }
    Write-Host "✅ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Error: Python is not installed or not in PATH." -ForegroundColor Red
    Write-Host "Please install Python 3.13+ from https://python.org" -ForegroundColor Yellow
    Write-Host "Make sure to check 'Add Python to PATH' during installation." -ForegroundColor Yellow
    exit 1
}

# Check Python version
try {
    $versionInfo = python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}')" 2>$null
    $version = [version]$versionInfo
    $requiredVersion = [version]"3.13.0"

    if ($version -lt $requiredVersion) {
        Write-Host "❌ Error: Python $requiredVersion or higher is required." -ForegroundColor Red
        Write-Host "Current version: $versionInfo" -ForegroundColor Red
        exit 1
    }
    Write-Host "✅ Python version $versionInfo is compatible" -ForegroundColor Green
} catch {
    Write-Host "❌ Error: Cannot determine Python version." -ForegroundColor Red
    exit 1
}

# Check if main.py exists
if (!(Test-Path "main.py")) {
    Write-Host "❌ Error: main.py not found in current directory." -ForegroundColor Red
    Write-Host "Please make sure you're running this script from the project root directory." -ForegroundColor Yellow
    exit 1
}

Write-Host "🚀 Starting Todo App..." -ForegroundColor Green
Write-Host ""

# Run the Python application
try {
    python main.py
    exit $LASTEXITCODE
} catch {
    Write-Host "❌ Error running the application: $_" -ForegroundColor Red
    exit 1
}
