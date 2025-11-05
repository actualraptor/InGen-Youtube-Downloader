# GitHub Release Checklist

## 📦 Files to Upload

Upload these files to your GitHub release:

### Required Files
- [ ] `InGen-YouTube-Downloader.exe` (from `dist/` folder)
  - Location: `C:\Scripts\YouTube Downloader\dist\InGen-YouTube-Downloader.exe`
  - Size: ~25-30MB

### Optional (but recommended)
- [ ] `RELEASE_NOTES_v1.0.md` (this describes the release)
- [ ] `README.md` (project overview)
- [ ] `QUICK_START.txt` (quick instructions)

## 📝 Release Information

### Release Title
```
v1.0.0 - "Welcome to Jurassic Park" 🦖
```

### Release Tag
```
v1.0.0
```

### Release Description (Copy/Paste)
```markdown
# 🦖 InGen YouTube Downloader - Initial Release

> _"Hold on to your butts!"_ - InGen Systems

## What's New

First public release of the Jurassic Park themed YouTube downloader!

### ✨ Features
- 🎨 Authentic Jurassic Park retro terminal UI
- 📥 Download videos in MP4, MP3, and WEBM formats
- 🔧 Smart dependency installer (installs yt-dlp and FFmpeg via UI)
- 💾 One-time download location setup
- 🦕 Customizable T-Rex image
- 📊 Smooth progress bars with live percentage
- 🎮 Keyboard shortcuts (F1-F4)

### 📦 What's Included
- **Standalone .exe** - No Python installation needed!
- **Bundled T-Rex image** - Customize by adding your own
- **Smart setup** - Only asks for download location once
- **Dependency manager** - Installs missing packages through the app

### 🚀 Quick Start
1. Download `InGen-YouTube-Downloader.exe`
2. Run it (first time: choose download location)
3. Press F3 to install dependencies
4. Paste a YouTube URL and press F1
5. Enjoy! 🦖

### 📋 System Requirements
- Windows 10 or later
- Internet connection
- ~150MB free space (including FFmpeg)

### 🐛 Known Issues
None! This is the first stable release.

### 📖 Full Documentation
See the [README](https://github.com/actualraptor/InGen-Youtube-Downloader) for complete instructions.

---

**Life finds a way... to download YouTube videos.** 🦕

Enjoy!
```

## 🔧 How to Create the Release

### Option 1: Via GitHub Website
1. Go to: https://github.com/actualraptor/InGen-Youtube-Downloader
2. Click "Releases" (right sidebar)
3. Click "Create a new release" or "Draft a new release"
4. Fill in:
   - **Tag:** `v1.0.0`
   - **Title:** `v1.0.0 - "Welcome to Jurassic Park" 🦖`
   - **Description:** Copy from above
5. Click "Attach binaries by dropping them here"
6. Upload `InGen-YouTube-Downloader.exe` from `dist/` folder
7. Check "This is a pre-release" if you want to test first
8. Click "Publish release"

### Option 2: Via Command Line (if you have Git installed)
```bash
# Tag the release
git tag -a v1.0.0 -m "Initial release - Welcome to Jurassic Park"
git push origin v1.0.0

# Then go to GitHub website to upload the .exe and add description
```

## ✅ Post-Release Checklist

After creating the release:

- [ ] Test the download link for the .exe
- [ ] Verify the .exe runs on a clean Windows machine
- [ ] Update README with installation instructions
- [ ] Share the release link
- [ ] Celebrate! 🎉🦖

## 📍 Important Files Location

All files are in: `C:\Scripts\YouTube Downloader\`

- **The .exe:** `dist\InGen-YouTube-Downloader.exe`
- **Release notes:** `RELEASE_NOTES_v1.0.md`
- **This checklist:** `RELEASE_CHECKLIST.md`

## 🎯 Direct Link to Create Release

Once your code is pushed to GitHub, create the release here:
https://github.com/actualraptor/InGen-Youtube-Downloader/releases/new

---

**You're all set!** Just follow the steps above to publish your release. 🦕



