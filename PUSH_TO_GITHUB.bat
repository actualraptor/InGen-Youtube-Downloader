@echo off
REM Quick script to push everything to GitHub
REM Repository: https://github.com/actualraptor/InGen-Youtube-Downloader

echo.
echo ========================================
echo   Pushing to GitHub
echo   Repository: InGen-Youtube-Downloader
echo ========================================
echo.

REM Initialize git if not already done
if not exist ".git" (
    echo Initializing Git repository...
    git init
    git branch -M main
)

REM Add remote if not already added
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo Adding remote origin...
    git remote add origin https://github.com/actualraptor/InGen-Youtube-Downloader.git
)

echo.
echo Adding all files...
git add .

echo.
echo Creating commit...
git commit -m "Add complete Jurassic Park themed YouTube downloader with professional documentation"

echo.
echo Pushing to GitHub...
git push -u origin main

echo.
echo ========================================
echo   Success! Repository updated
echo   View at: https://github.com/actualraptor/InGen-Youtube-Downloader
echo ========================================
echo.

pause

