# 🦖 System Diagnostics - Dependency Checker

## New Feature: Automatic Dependency Management!

The Jurassic Park GUI now includes a built-in **System Diagnostics** feature that checks for and installs missing dependencies!

---

## 🎮 How To Use

### **Method 1: Use the System Diagnostics Button**

1. Launch the GUI (`run_gui.bat` or `python youtube_downloader_gui.py`)
2. Click the green **"<F3> SYSTEM DIAGNOSTICS"** button (or press **F3**)
3. Watch the Jurassic Park themed console output as it scans for modules:

```
> ====================================
> SYSTEM DIAGNOSTICS INITIATED
> ====================================
> Scanning system modules...
> 
> Checking YouTube Downloader Engine...
>   [yt_dlp] .............. OK
> Checking Image Processing System...
>   [PIL] .............. OK
> Checking Progress Indicator...
>   [tqdm] .............. OK
> 
> ====================================
> STATUS: ALL SYSTEMS OPERATIONAL
> ====================================
```

4. If dependencies are missing, you'll see:
```
>   [yt_dlp] .............. MISSING!
> 
> ====================================
> STATUS: 2 CRITICAL MODULES MISSING
> ====================================
```

5. A dialog will ask if you want to install them - click **Yes**
6. Watch as they install in real-time with progress!
7. Restart the application when complete

---

### **Method 2: Automatic Check When Downloading**

If you try to download without `yt-dlp` installed:
1. Click **"<F1> INITIATE"** to start a download
2. If `yt-dlp` is missing, you'll get a prompt
3. Click **Yes** to run System Diagnostics
4. Follow the installation prompts

---

## 🔧 What Gets Checked

The system checks for these critical modules:

| Module | Package Name | Description |
|--------|-------------|-------------|
| `yt_dlp` | `yt-dlp` | YouTube Downloader Engine |
| `PIL` | `Pillow` | Image Processing System |
| `tqdm` | `tqdm` | Progress Indicator |

---

## 🎨 Jurassic Park Themed Output

The console output uses authentic JP terminal styling:

- **Amber text** on black background
- **Dotted lines** like the movie (`..........`)
- **Status indicators** (`OK`, `MISSING!`, `INSTALLED`)
- **System messages** with proper formatting
- **Progress bar** shows during installation

---

## ⌨️ Keyboard Shortcuts

- **F1** - Initiate Download
- **F2** - Choose Formats
- **F3** - System Diagnostics ⭐

---

## 🔄 Installation Process

When you choose to install missing dependencies:

```
> ====================================
> DEPENDENCY INSTALLATION INITIATED
> ====================================
> 
> Installing yt-dlp...
>   yt-dlp .............. INSTALLED
> Installing Pillow...
>   Pillow .............. INSTALLED
> 
> ====================================
> INSTALLATION COMPLETE
> ====================================
> Please restart the application
```

---

## 💡 Technical Details

### How It Works
1. Uses `importlib.util.find_spec()` to check if modules exist
2. Runs `pip install` via `subprocess` if missing
3. Shows real-time installation progress in the console
4. Uses threading to prevent GUI freezing
5. Re-enables buttons after installation

### Safe and Reliable
- ✅ Only installs what's actually missing
- ✅ Shows exactly what will be installed before proceeding
- ✅ Uses your current Python environment
- ✅ Provides clear error messages if something fails

---

## 🚨 Troubleshooting

### "Installation Failed"
- Make sure you have internet connection
- Try running the application as administrator
- Check if pip is installed: `python -m pip --version`

### "Please restart the application"
- Close the GUI completely
- Relaunch using `run_gui.bat`
- The new modules will now be available

### Still Having Issues?
- Manually install from command line:
  ```bash
  cd "C:\Scripts\YouTube Downloader"
  .venv\Scripts\activate
  pip install -r requirements.txt
  ```

---

## 🎯 First Time Setup

**Recommended workflow:**

1. Launch GUI for the first time
2. Press **F2** (System Diagnostics)
3. Install any missing dependencies
4. Restart the application
5. You're ready to download! 🦕

---

## 📝 Note

FFmpeg is still required for audio conversion (MP3, OGG, M4A) but must be installed separately:
- `winget install ffmpeg` (Windows)
- Or download from: https://ffmpeg.org/download.html

The System Diagnostics tool checks **Python packages only**, not system utilities like FFmpeg.

---

**"Hold onto your butts... while we install these dependencies!"** 🦖⚡

