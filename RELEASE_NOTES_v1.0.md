# 🦖 InGen YouTube Downloader v1.0 - Initial Release

> _"Hold on to your butts!"_ - InGen Systems, 1993

## 🎬 What is This?

A **Jurassic Park themed YouTube downloader** with a retro terminal aesthetic inspired by the classic 1993 film. Download YouTube videos in multiple formats with style!

## ✨ Features

### 🎨 Authentic Jurassic Park UI
- Retro terminal interface with amber/orange and green color scheme
- Animated blinking "LIVE FEED" indicator
- Custom Jurassic Park themed dialogs (no boring Windows pop-ups!)
- Customizable T-Rex image (place your own in the `img/` folder)
- Real-time "Isla Nublar" timestamp display

### 📥 Download Capabilities
- **Supported Formats:**
  - MP4 (1080p, 720p, 480p, 360p)
  - MP3 (Audio only)
  - WEBM (Original quality)
- Smooth progress bar with real-time percentage
- Live console output showing download status
- Cancel downloads anytime

### 🔧 Smart Dependency Management
- Built-in dependency checker (`F3` - System Diagnostics)
- Automatic installation of required packages (`yt-dlp`)
- FFmpeg installation helper (required for MP3 conversion)
- All installations happen through the Jurassic Park themed interface

### 💾 First Run Setup
- One-time download location setup on first launch
- Config saved automatically for future runs
- Change download location anytime with `F4`
- No repeated configuration needed

## 📦 Installation

### Quick Start
1. Download `InGen-YouTube-Downloader.exe` from the releases page
2. Double-click to run - **no Python installation needed!**
3. Choose your download location (first time only)
4. Press `F3` to check and install dependencies
5. Start downloading! 🦖

### System Requirements
- **OS:** Windows 10 or later
- **Storage:** ~50MB for application + 100MB for FFmpeg (optional)
- **Internet:** Required for downloading videos and installing dependencies

## 🎮 How to Use

### Quick Guide
1. **Launch** the application
2. **Paste** a YouTube URL in the input field
3. **Choose** format with `F2` (MP4, MP3, or WEBM)
4. **Click** `F1 - INITIATE` to start download
5. **Watch** the progress bar and console output

### Keyboard Shortcuts
- `F1` - Initiate Download
- `F2` - Choose Format
- `F3` - System Diagnostics (check/install dependencies)
- `F4` - Change Download Location
- `CANCEL OPERATION` - Stop current download

### First Time Setup
On first launch, the application will ask where to save downloads:
- Click **YES** to choose a custom folder
- Click **NO** to use the default location (next to the .exe)

This setting is saved and only asked once!

## 🔨 Dependencies

### Included (Bundled in .exe)
✅ Python runtime  
✅ tkinter GUI framework  
✅ Pillow image library  
✅ All core code and T-Rex image

### Installable via App
📦 **yt-dlp** - YouTube video downloader (install via `F3`)  
📦 **FFmpeg** - Media converter (install via `F3`, required for MP3)

**Note:** FFmpeg is required for MP3 conversion. MP4 and WEBM work without it!

## 🎨 Customization

### Custom T-Rex Image
1. Place your custom image in the `img/` folder (next to the .exe)
2. Name it one of:
   - `trex.png`
   - `trex.jpg`
   - `trex.gif`
3. Restart the application
4. Your custom image will appear!

**Recommended:** Square images, 200-300px, green/transparent background

## 🐛 Troubleshooting

### "Module yt_dlp not found"
→ Press `F3` to open System Diagnostics and install dependencies

### "FFmpeg not found" (when downloading MP3)
→ Press `F3` and install FFmpeg through the app

### Downloads aren't starting
→ Check your internet connection and YouTube URL

### Want to change download location?
→ Press `F4` to choose a new folder

## 📝 Technical Details

### What's Inside the .exe?
- Python 3.12 runtime
- All required Python libraries
- Jurassic Park themed GUI
- T-Rex image (customizable)
- Config management system

### File Size
- **Application:** ~25-30MB (includes Python runtime)
- **FFmpeg:** ~100MB (optional, installed separately)

### Where are files saved?
- **config.ini** - Next to the .exe (saves your download location)
- **Downloads** - Location you chose on first run (default: `downloads/` folder)

## 🚀 For GitHub Users

Want to contribute or build from source? Check out:
- `README.md` - Full project documentation
- `CONTRIBUTING.md` - How to contribute
- `CODE_OF_CONDUCT.md` - Community guidelines
- `docs/` - Detailed guides and API documentation

## 🙏 Credits

- **yt-dlp** - The amazing YouTube downloader library
- **FFmpeg** - The universal media converter
- **Jurassic Park** - For the iconic aesthetic
- **Steven Spielberg** - For creating the Jurassic Park universe

## 📜 License

MIT License - Free to use, modify, and distribute!

---

## 🦖 Final Words

_"Life finds a way... to download YouTube videos."_

Welcome to InGen Systems. Enjoy downloading videos with style! 

If you encounter any issues or have suggestions, please open an issue on GitHub.

**Happy Downloading!** 🎬🦕

---

**Release Date:** November 5, 2025  
**Version:** 1.0.0  
**Build:** Initial Public Release  
**Codename:** "Welcome to Jurassic Park"


