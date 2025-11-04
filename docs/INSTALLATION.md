# Installation Guide

Complete installation instructions for InGen Systems - YouTube Retrieval Console.

## Table of Contents
- [System Requirements](#system-requirements)
- [Quick Installation](#quick-installation)
- [Manual Installation](#manual-installation)
- [Portable Installation](#portable-installation)
- [Troubleshooting](#troubleshooting)

## System Requirements

### Minimum Requirements
- **Operating System**: Windows 10 (1809 or later) or Windows 11
- **Python**: 3.8 or higher
- **RAM**: 2 GB
- **Disk Space**: 500 MB (including dependencies)
- **Internet**: Required for downloads

### Recommended
- **Operating System**: Windows 11
- **Python**: 3.10 or higher
- **RAM**: 4 GB or more
- **Disk Space**: 1 GB or more
- **Display**: 1024x768 or higher resolution

## Quick Installation

The easiest way to get started:

1. **Download the project**
   - Download ZIP from GitHub or clone the repository
   ```bash
   git clone https://github.com/yourusername/jurassic-youtube-downloader.git
   ```

2. **Navigate to the folder**
   ```bash
   cd jurassic-youtube-downloader
   ```

3. **Run the launcher**
   - Double-click `run_gui.bat`
   - OR from command line: `run_gui.bat`

4. **Wait for setup**
   - The launcher will automatically:
     - Create a virtual environment
     - Install required Python packages
     - Launch the GUI

5. **First run**
   - Press **F3** to run System Diagnostics
   - Install any missing dependencies
   - Optionally install FFmpeg for MP3 support

That's it! You're ready to download videos. 🦖

## Manual Installation

If you prefer more control:

### Step 1: Install Python

1. Download Python 3.8+ from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important**: Check "Add Python to PATH"
4. Click "Install Now"

### Step 2: Verify Python Installation

```bash
python --version
```
Should show Python 3.8 or higher.

### Step 3: Download the Project

```bash
git clone https://github.com/yourusername/jurassic-youtube-downloader.git
cd jurassic-youtube-downloader
```

Or download ZIP and extract.

### Step 4: Create Virtual Environment

```bash
python -m venv .venv
```

### Step 5: Activate Virtual Environment

```bash
.venv\Scripts\activate
```

You should see `(.venv)` in your command prompt.

### Step 6: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- yt-dlp
- Pillow
- tqdm

### Step 7: Run the Application

```bash
python youtube_downloader_gui.py
```

## Installing FFmpeg (Optional)

FFmpeg is required for MP3 downloads. You have several options:

### Option 1: In-App Installation (Easiest)
1. Launch the application
2. Press **F3** (System Diagnostics)
3. If FFmpeg is missing, click "Yes" to install
4. Restart the application

### Option 2: Manual Installation via winget
```bash
winget install Gyan.FFmpeg
```

### Option 3: Manual Installation via Chocolatey
```bash
choco install ffmpeg
```

### Option 4: Manual Download
1. Download from [ffmpeg.org](https://ffmpeg.org/download.html)
2. Extract to a folder (e.g., `C:\ffmpeg`)
3. Add to PATH:
   - Open System Properties → Environment Variables
   - Edit PATH
   - Add `C:\ffmpeg\bin`
   - Click OK

### Verify FFmpeg Installation
```bash
ffmpeg -version
```

## Portable Installation

Want to run on a USB drive or without installation?

1. Copy the entire project folder to your portable drive
2. Ensure Python is installed on the target machine
3. Run `run_gui.bat` as usual
4. The virtual environment will be created in the folder

## Troubleshooting

### Python Not Found

**Problem**: `python is not recognized as an internal or external command`

**Solution**:
1. Reinstall Python with "Add to PATH" checked
2. Or manually add Python to PATH
3. Or use full path: `C:\Python310\python.exe`

### Permission Denied

**Problem**: Permission errors when creating virtual environment

**Solution**:
- Run Command Prompt as Administrator
- Or install in a folder with write permissions (e.g., Documents)

### pip Install Fails

**Problem**: Dependencies fail to install

**Solution**:
1. Update pip: `python -m pip install --upgrade pip`
2. Try again: `pip install -r requirements.txt`
3. Check internet connection
4. Try installing packages individually:
   ```bash
   pip install yt-dlp
   pip install Pillow
   pip install tqdm
   ```

### Virtual Environment Won't Activate

**Problem**: `.venv\Scripts\activate` doesn't work

**Solution**:
1. Use PowerShell instead of CMD
2. Or use: `.venv\Scripts\activate.bat`
3. Or run directly: `.venv\Scripts\python.exe youtube_downloader_gui.py`

### GUI Doesn't Start

**Problem**: Window doesn't appear

**Solution**:
1. Check for errors in console
2. Verify tkinter is installed: `python -m tkinter`
3. Reinstall Python with tkinter support
4. Try running: `python youtube_downloader_gui.py` directly

### Missing Dependencies Dialog Appears

**Problem**: App says dependencies are missing

**Solution**:
- Press **F3** to run System Diagnostics
- Install missing packages from within the app
- Or manually: `pip install <package-name>`

## Uninstallation

To remove the application:

1. Delete the project folder
2. (Optional) Remove Python if no longer needed
3. (Optional) Remove FFmpeg if installed

The application doesn't install anything outside its folder except for dependencies in the virtual environment.

## Updating

To update to the latest version:

```bash
cd jurassic-youtube-downloader
git pull origin main
pip install -r requirements.txt --upgrade
```

Or download the latest ZIP and replace files.

---

Need more help? Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) or open an issue on GitHub.

