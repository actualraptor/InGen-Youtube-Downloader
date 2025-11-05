# Usage Guide

Complete guide to using InGen Systems - YouTube Retrieval Console.

## Table of Contents
- [Getting Started](#getting-started)
- [Basic Operations](#basic-operations)
- [Advanced Features](#advanced-features)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Tips and Tricks](#tips-and-tricks)

## Getting Started

### First Launch

1. Run `run_gui.bat` or `python youtube_downloader_gui.py`
2. The Jurassic Park themed interface will appear
3. You'll see:
   - A blinking red **LIVE FEED** indicator
   - The main input field for URLs
   - Four control buttons
   - A T-Rex image (or dinosaur emoji)
   - Status display and console output

### Understanding the Interface

```
┌─────────────────────────────────────────────────────────┐
│  InGen Systems - Isla Nublar YouTube Retrieval Console │
│  ● LIVE FEED                            11-06-1993 HH:MM│
├─────────────────────────────────────────────────────────┤
│  ENTER TARGET URL:                                      │
│  [____________________________]                         │
│  [F1 INITIATE] [CANCEL] [F2 FORMATS] [F3 DIAGNOSTICS]  │
├──────────────┬──────────────────────────────────────────┤
│    🦖        │  Ready to initialize...                  │
│              │                                          │
│              │  DOWNLOAD PROGRESS: ████ 0%             │
├──────────────┴──────────────────────────────────────────┤
│  CHARGING...                                            │
│  ████████████████████████░░░░                          │
│  ENERGY LEVELS                                          │
├─────────────────────────────────────────────────────────┤
│  > Booting up processes...                             │
│  > Analyzing target...                                 │
│  > System ready                                        │
└─────────────────────────────────────────────────────────┘
```

## Basic Operations

### Downloading a Video

1. **Copy the YouTube URL**
   - Go to YouTube
   - Find the video you want
   - Copy the URL from the address bar

2. **Paste the URL**
   - Click in the URL input field
   - Press `Ctrl+V` to paste
   - Or right-click → Paste

3. **Start Download**
   - Press **F1** or click **INITIATE**
   - Watch the progress bars fill
   - Monitor console output for status

4. **Wait for Completion**
   - Progress shows in real-time
   - Console displays detailed status
   - Download complete message appears

5. **Find Your File**
   - Files save to `downloads/` folder
   - Named automatically based on video title

### Choosing Format

Before downloading, select your preferred format:

1. **Open Format Selection**
   - Press **F2** or click **CHOOSE FORMATS**

2. **Select Format**
   - **MP4**: Video file (most common)
   - **MP3**: Audio only (requires FFmpeg)
   - **WEBM**: Alternative video format

3. **Choose Quality**
   - **Best**: Highest quality available
   - **1080p**: Full HD (if available)
   - **720p**: HD
   - **Audio Only**: Sound only (smallest file)

4. **Confirm**
   - Click **OK** to save settings
   - Or **Cancel** to keep current settings

### Canceling a Download

If you need to stop:

1. Click **CANCEL OPERATION** button
2. Download stops immediately
3. Partial files may remain in downloads folder
4. Interface returns to ready state

## Advanced Features

### System Diagnostics (F3)

Check and install dependencies:

1. **Press F3** or click **SYSTEM DIAGNOSTICS**

2. **Review Results**
   - Green "OK" = Installed
   - Red "MISSING" = Not installed
   - Console shows detailed status

3. **Install Missing Packages**
   - If prompted, click "Yes"
   - Wait for installation
   - Restart app if needed

### Installing FFmpeg

For MP3 downloads, you need FFmpeg:

1. Press **F3** for diagnostics
2. If FFmpeg is missing, you'll see a themed dialog
3. Click **Yes** to auto-install (uses winget)
4. Wait 2-5 minutes for installation
5. Restart the application
6. MP3 format now available!

### Custom T-Rex Image

Personalize your interface:

1. Create an `img` folder in the project directory
2. Add your image:
   - Name it `trex.png` (or .jpg, .gif)
   - Recommended size: 240x240 pixels
   - Any dinosaur or JP-themed image works!
3. Restart the application
4. Your custom image appears in the left panel

### Using the Console Output

The console provides detailed information:

- **Blue/Amber text**: Status messages
- **Green text**: Success messages
- **Red text**: Error messages
- **Progress updates**: Real-time percentage
- **File info**: Title, duration, format

## Keyboard Shortcuts

Master these for faster workflow:

| Key | Action | Description |
|-----|--------|-------------|
| **F1** | Initiate Download | Start downloading the URL |
| **F2** | Choose Format | Open format selection dialog |
| **F3** | System Diagnostics | Check dependencies |
| **Ctrl+V** | Paste URL | Paste from clipboard |
| **Ctrl+A** | Select All | Select all text in URL field |
| **Esc** | Cancel Dialog | Close format/diagnostic dialogs |

## Tips and Tricks

### 1. Batch Downloads
While the app doesn't support playlists yet, you can:
- Download one video
- Paste next URL immediately after completion
- Repeat for multiple videos

### 2. Organizing Downloads
Create subfolders in `downloads/`:
```
downloads/
  ├── Music/
  ├── Tutorials/
  ├── Entertainment/
  └── Archive/
```

### 3. Best Quality Downloads
For highest quality:
1. Press F2
2. Select "best" quality
3. Choose MP4 or WEBM
4. These formats preserve original quality

### 4. Audio Extraction
To get audio from videos:
1. Install FFmpeg (F3 → System Diagnostics)
2. Press F2
3. Select MP3 format
4. Downloads as audio file

### 5. Handling Long Videos
For very long videos (1+ hour):
- Be patient during analysis
- Progress may appear slow at first
- Console shows "Retrieving video information..."
- Wait for actual download to begin

### 6. Fixing Stuck Downloads
If download seems stuck:
1. Check console for errors
2. Click **CANCEL OPERATION**
3. Check internet connection
4. Try a different format
5. Restart the application

### 7. Updating yt-dlp
Keep the download engine updated:
```bash
.venv\Scripts\pip install --upgrade yt-dlp
```

### 8. Speed Optimization
- Close other bandwidth-heavy applications
- Use wired connection instead of WiFi
- Choose lower quality for faster downloads
- Ensure antivirus isn't scanning downloads folder

## Common Workflows

### Quick Music Download
```
1. Copy YouTube music video URL
2. Press F2 → Select MP3 → OK
3. Paste URL (Ctrl+V)
4. Press F1
5. Done! Audio in downloads/
```

### HD Video Archive
```
1. Press F2 → Select MP4, 1080p → OK
2. Paste video URL
3. Press F1
4. Wait for completion
5. Move to archive folder
6. Repeat for next video
```

### First Time Setup
```
1. Launch application
2. Press F3 (System Diagnostics)
3. Install any missing dependencies
4. Install FFmpeg if you want MP3
5. Add custom T-Rex image (optional)
6. Press F2 to set default format
7. Ready to download!
```

## Troubleshooting Quick Reference

| Problem | Quick Fix |
|---------|-----------|
| Can't start download | Press F3, install dependencies |
| MP3 fails | Press F3, install FFmpeg |
| Slow download | Check internet, try lower quality |
| Wrong format | Press F2 before downloading |
| App frozen | Wait 30 seconds, or restart |
| Can't find file | Check `downloads/` folder |

---

For more detailed troubleshooting, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

*"Life finds a way... to download videos efficiently."* 🦖


