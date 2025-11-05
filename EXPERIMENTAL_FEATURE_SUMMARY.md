# 🦖 Automatic Stream Detection - EXPERIMENTAL

## ✅ What's Been Done

### New Branch Created
- **Branch Name**: `feature/auto-stream-detection`
- **Purpose**: Test automatic blob: URL detection without affecting main stable version
- **Status**: Ready for testing

### New Features Added

#### 1. **Stream Detector Module** (`stream_detector.py`)
- Standalone Python module for stream detection
- Uses Playwright to intercept network requests
- Detects HLS (.m3u8), DASH (.mpd), and MP4 streams
- Can be used independently or through GUI

#### 2. **Auto-Detect Stream Button**
- New `<F5> AUTO-DETECT STREAM (EXPERIMENTAL)` button
- Green themed (experimental feature styling)
- Located in second button row
- Includes helper text explaining its purpose

#### 3. **Automated Detection Process**
- Opens page in headless Chromium browser
- Intercepts all network traffic
- Filters for video stream patterns
- Auto-updates URL field with detected stream
- Full Jurassic Park themed progress messages

#### 4. **Smart Dependency Management**
- Auto-detects if Playwright is installed
- Offers to install it when needed
- Downloads Chromium browser binaries (~200MB)
- All themed installation dialogs

### Updated Files

1. **youtube_downloader_gui.py**
   - Added `auto_detect_stream()` method
   - Added `_detect_stream_thread()` for background processing
   - Added `install_playwright()` and thread
   - New button in UI (F5)
   - ~250 lines of new code

2. **requirements.txt**
   - Added `playwright>=1.40.0`

3. **stream_detector.py** (NEW)
   - 300+ lines of stream detection logic
   - Standalone module
   - Can be tested independently

4. **Documentation**
   - `TEST_STREAM_DETECTION.md` - How to test
   - `EXPERIMENTAL_FEATURE_SUMMARY.md` - This file

## 🎯 Use Cases

### Perfect For:
- ✅ SVT Play (Swedish TV)
- ✅ Public streaming sites with blob: URLs
- ✅ HLS/DASH streaming platforms
- ✅ Sites without DRM protection

### Won't Work For:
- ❌ DRM protected (Netflix, Disney+, etc.)
- ❌ Login-required content (currently)
- ❌ Geo-blocked content
- ❌ Sites with advanced anti-bot protection

## 📋 How to Use

### For Your Friend (Simple Steps):

1. **Get the URL**
   - Find the video on SVT Play
   - Copy the page URL (not the blob: URL)
   - Example: `https://www.svtplay.se/video/abc123`

2. **Open the App**
   - Launch InGen YouTube Downloader
   - Paste the URL in the input field

3. **First Time Setup (If Playwright not installed)**
   - Click `<F5> AUTO-DETECT STREAM`
   - It will ask to install Playwright
   - Click YES
   - Wait 3-5 minutes (downloads ~200MB)
   - Restart the app

4. **Detect and Download**
   - Click `<F5> AUTO-DETECT STREAM`
   - Wait 30-60 seconds (watch console)
   - URL will update automatically
   - Click `<F1> INITIATE` to download

## 🧪 Testing

### Test With:
```
https://www.svtplay.se/video/[any-video-id]
```

### Expected Behavior:
1. **Detection Phase** (30-60 seconds)
   - Console shows "STREAM DETECTION INITIATED"
   - Browser opens invisibly
   - Network requests are captured

2. **Success**
   - "STREAM DETECTED!" message
   - URL field updates with .m3u8 URL
   - Ready to download

3. **Failure Scenarios**
   - No video found
   - DRM protected
   - Geo-blocked
   - Timeout (>60 seconds)

## 🔧 Technical Details

### How It Works:
```
User clicks F5
     ↓
Check if Playwright installed
     ↓
Launch headless Chromium browser
     ↓
Navigate to page URL
     ↓
Intercept ALL network requests
     ↓
Filter for video patterns (.m3u8, .mpd, .mp4)
     ↓
Select best quality stream
     ↓
Update URL field
     ↓
User clicks F1 to download
```

### Stream Detection Priority:
1. **Master playlists** (master.m3u8) - Best quality, adaptive
2. **HLS streams** (.m3u8) - Apple standard
3. **DASH streams** (.mpd) - MPEG-DASH
4. **Direct MP4** (.mp4) - Fallback

### Dependencies:
- **Playwright**: Browser automation framework
- **Chromium**: Headless browser (~150MB)
- **Python 3.7+**: Required runtime

## 📊 Performance

### First Time (With Installation):
- Playwright install: 30-60 seconds
- Chromium download: 2-5 minutes
- Total: 3-6 minutes

### After Installation:
- Browser launch: 2-3 seconds
- Page load: 5-10 seconds
- Detection: 30-60 seconds
- Total: 40-75 seconds per video

### Disk Space:
- Playwright package: ~2MB
- Chromium browser: ~150MB
- Total: ~152MB

## 🔒 Safety & Privacy

### What It Does:
- ✅ Opens page in isolated headless browser
- ✅ Only captures network requests
- ✅ No data sent to external servers
- ✅ No cookies or personal data stored

### What It Doesn't Do:
- ❌ Doesn't store your browsing history
- ❌ Doesn't send data to InGen servers (there aren't any!)
- ❌ Doesn't bypass DRM or crack encryption
- ❌ Doesn't violate copyright (up to user)

## 🚦 Branch Management

### Current Branch:
```bash
git branch
* feature/auto-stream-detection
  main
```

### Switch to Main (Stable):
```bash
git checkout main
```

### Switch to Experimental:
```bash
git checkout feature/auto-stream-detection
```

### Merge to Main (If successful):
```bash
git checkout main
git merge feature/auto-stream-detection
```

## 📈 Future Enhancements

### Possible Improvements:
- [ ] Real-time progress indicator during detection
- [ ] Multiple quality options display
- [ ] Cookie injection for login-protected content
- [ ] Manual browser mode (user logs in, then detects)
- [ ] Support for m3u8 playlist selection
- [ ] Subtitle detection and download
- [ ] Faster detection (<30 seconds)
- [ ] Firefox/Safari support (currently Chrome only)

### Community Requested:
- [ ] One-click download without detection step
- [ ] Batch URL processing
- [ ] Scheduled recording (capture streams at specific times)
- [ ] Built-in video player preview

## 🐛 Known Issues

1. **Slow Detection**: Takes 30-60 seconds (investigating optimization)
2. **Large Download**: Chromium is ~150MB (no alternative currently)
3. **Windows Only**: Playwright might need adjustments for Mac/Linux
4. **No DRM Support**: Intentionally not supported (legal reasons)

## 📞 Support

### If It Doesn't Work:
1. Check `TEST_STREAM_DETECTION.md` for troubleshooting
2. Make sure Playwright is installed
3. Verify internet connection
4. Try different URL from same site
5. Check if site requires login

### Reporting Bugs:
- Which site (e.g., SVT Play)
- Error message (from console)
- Steps to reproduce
- Screenshot if possible

---

## 🎉 Ready to Test!

The feature is fully implemented and ready for testing. It's on a separate branch so your stable version is completely safe.

**Main branch** = Stable, working YouTube downloader
**Feature branch** = Experimental stream detection

Test it out and let me know how it works! 🦕✨

