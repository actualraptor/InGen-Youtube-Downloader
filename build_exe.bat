@echo off
REM Build InGen YouTube Downloader as standalone .exe

echo.
echo ========================================
echo   Building InGen YouTube Downloader
echo   Standalone Executable
echo ========================================
echo.

REM Check if virtual environment is active
if not exist ".venv\Scripts\activate.bat" (
    echo [!] Virtual environment not found!
    echo [*] Creating virtual environment...
    python -m venv .venv
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

echo [*] Installing build dependencies...
pip install pyinstaller pillow yt-dlp tqdm

echo.
echo [*] Building executable...
echo This may take a few minutes...
echo.

REM Build using spec file
pyinstaller build_exe.spec --clean --noconfirm

echo.
echo ========================================
echo   Build Complete!
echo ========================================
echo.

if exist "dist\InGen-YouTube-Downloader.exe" (
    echo [SUCCESS] Executable created at:
    echo   dist\InGen-YouTube-Downloader.exe
    echo.
    echo [*] File size: 
    for %%A in ("dist\InGen-YouTube-Downloader.exe") do echo   %%~zA bytes
    echo.
    echo [*] You can now distribute this .exe file!
    echo [*] It includes everything needed to run.
    echo.
    echo [*] To test it, run:
    echo     dist\InGen-YouTube-Downloader.exe
) else (
    echo [ERROR] Build failed! Check the output above for errors.
)

echo.
pause




