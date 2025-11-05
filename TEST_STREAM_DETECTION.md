# Testing Stream Auto-Detection Feature 🦖

## Feature Branch: `feature/auto-stream-detection`

This experimental feature automatically detects real stream URLs from pages that use blob: URLs.

## What It Does

1. **Intercepts Network Traffic**: Uses Playwright to open the page in a headless browser
2. **Captures Stream URLs**: Detects .m3u8, .mpd, .ts, and .mp4 URLs
3. **Auto-Updates URL**: Replaces the page URL with the detected stream URL
4. **Ready to Download**: After detection, click INITIATE to download

## Test URL

```
https://www.svtplay.se/video/[VIDEO_ID]
```

## How to Test

### Step 1: Launch the GUI

```bash
cd "C:\Scripts\YouTube Downloader"
.venv\Scripts\python.exe youtube_downloader_gui.py
```

### Step 2: Install Playwright (First Time Only)

1. Paste the SVT Play URL in the input field
2. Click `<F5> AUTO-DETECT STREAM`
3. It will ask to install Playwright (~200MB)
4. Click YES to install
5. Wait 2-5 minutes for download
6. Restart the app after installation

### Step 3: Detect the Stream

1. Paste the SVT Play URL in the input field
2. Click `<F5> AUTO-DETECT STREAM`
3. Wait 30-60 seconds (watch the console)
4. The URL field will update with the .m3u8 stream URL
5. Click `<F1> INITIATE` to download

## Expected Output

### Console Log:
```
> ====================================
> STREAM DETECTION INITIATED
> ====================================
> 
> Target URL: https://www.svtplay.se/video/...
> 
> Opening page in headless browser...
> Intercepting network requests...
> This may take 30-60 seconds...
> 
> Analyzing page...
> 
> ====================================
> STREAM DETECTED!
> ====================================
> 
> Stream Type: M3U8
> Stream URL: https://...master.m3u8
> 
> Found 3 total stream(s)
> 
> URL updated! You can now click INITIATE to download.
```

## Known Limitations

1. **DRM Protected Content**: Won't work (Disney+, Netflix, etc.)
2. **Login Required**: Must be publicly accessible
3. **Geo-Blocked**: Might fail if content is region-locked
4. **Slow**: Takes 30-60 seconds to analyze
5. **Large Download**: Playwright + Chromium = ~200MB

## Technical Details

### New Files:
- `stream_detector.py` - Core detection logic
- Updated `youtube_downloader_gui.py` - Added F5 button and methods
- Updated `requirements.txt` - Added Playwright

### How It Works:
1. Playwright launches Chromium in headless mode (invisible)
2. Navigates to the target page
3. Intercepts all network requests
4. Filters for video stream patterns (.m3u8, .mpd, etc.)
5. Returns the best quality stream URL
6. Updates the GUI with the detected URL

### Stream Detection Priority:
1. .m3u8 master playlists (HLS - best)
2. .mpd files (DASH)
3. .mp4 direct files
4. .ts transport streams

## Troubleshooting

### "Playwright not installed"
- Click YES when prompted
- Wait for installation
- Restart app

### "No streams detected"
- Check if page has a video
- Try a different video on the same site
- Check if site requires login
- Some sites use DRM (won't work)

### "Detection takes too long"
- It's normal (30-60 seconds)
- Watch console for progress
- If it hangs > 2 minutes, cancel and restart

### "Stream detected but download fails"
- Some streams require special headers
- Try different quality settings
- Check if FFmpeg is installed

## Switching Back to Main Branch

If you want to go back to the stable version:

```bash
git checkout main
```

To return to this feature:

```bash
git checkout feature/auto-stream-detection
```

## Future Improvements

- [ ] Progress bar during detection
- [ ] Multiple stream quality selection
- [ ] Cookie/session support for login-protected content
- [ ] Faster detection (currently 30-60s)
- [ ] Support for more streaming protocols
- [ ] Built-in browser for manual login before detection

---

**Status**: 🧪 EXPERIMENTAL - Use with caution!

This feature is on a separate branch and won't affect your main stable version.

