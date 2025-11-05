@echo off
REM YouTube Downloader Launcher
REM This script activates the virtual environment and runs the downloader

echo.
echo ========================================
echo   YouTube Downloader
echo ========================================
echo.

REM Check if virtual environment exists
if not exist ".venv\Scripts\activate.bat" (
    echo [!] Virtual environment not found!
    echo [*] Creating virtual environment...
    python -m venv .venv
    if errorlevel 1 (
        echo [X] Failed to create virtual environment
        pause
        exit /b 1
    )
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Check if dependencies are installed
python -c "import yt_dlp" 2>nul
if errorlevel 1 (
    echo [*] Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [X] Failed to install dependencies
        pause
        exit /b 1
    )
)

REM Run the downloader
echo [*] Starting YouTube Downloader...
echo.
python youtube_downloader.py

REM Keep window open
echo.
pause




