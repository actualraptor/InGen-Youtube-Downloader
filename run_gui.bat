@echo off
REM InGen Systems - YouTube Retrieval Console Launcher
REM Jurassic Park themed GUI

echo.
echo ========================================
echo   InGen Systems - Isla Nublar
echo   YouTube Retrieval Console
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

REM Run the GUI downloader (pythonw.exe hides the console window)
echo [*] Launching Jurassic Park Interface...
echo.
start "" ".venv\Scripts\pythonw.exe" "youtube_downloader_gui.py"
exit

