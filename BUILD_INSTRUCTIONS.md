# Building Standalone Executable

Create a standalone `.exe` file that can run on any Windows computer without Python installed!

## Quick Build

Just double-click:
```
build_exe.bat
```

The executable will be created in the `dist/` folder.

## What Gets Included

The `.exe` file includes:
- ✅ All Python code
- ✅ All required libraries (yt-dlp, Pillow, tkinter)
- ✅ T-Rex image from `img/` folder
- ✅ Jurassic Park theme
- ✅ FFmpeg installation capability

## Requirements

- Python 3.8+ installed
- Internet connection (for downloading dependencies)
- ~500MB disk space for build

## Manual Build Steps

If the batch file doesn't work:

1. **Install PyInstaller**
```bash
.venv\Scripts\activate
pip install pyinstaller pillow yt-dlp tqdm
```

2. **Build the executable**
```bash
pyinstaller build_exe.spec --clean --noconfirm
```

3. **Find your executable**
```
dist\InGen-YouTube-Downloader.exe
```

## First Run Experience

When users run the `.exe` for the first time:

1. **Welcome dialog** appears
2. **Choose download location** (or use default)
3. **App launches** with Jurassic Park interface
4. **System Diagnostics (F3)** can install FFmpeg if needed

## Features in Standalone Version

### ✅ Works Without Python
- No Python installation needed
- No pip, no virtual environments
- Just run the `.exe`!

### ✅ Portable
- Can run from USB drive
- Can run from any folder
- Config saves next to `.exe`

### ✅ All Features Included
- Download MP4, MP3, WEBM
- Change download location (F4)
- Install FFmpeg via System Diagnostics (F3)
- Custom T-Rex image bundled
- All keyboard shortcuts work

### ✅ User-Friendly
- First-run setup wizard
- Saves download location preference
- No technical knowledge required

## Distribution

### Sharing Your .exe

After building, you can share:
```
dist/InGen-YouTube-Downloader.exe  (your executable)
```

**Recommended**: Create a release package:
```
InGen-YouTube-Downloader-v1.0.0/
├── InGen-YouTube-Downloader.exe
├── README.txt (quick start guide)
└── img/ (optional, for custom images)
```

### File Size

Expect the `.exe` to be around:
- **50-80 MB** (includes Python runtime + libraries)
- This is normal for Python applications

### Antivirus Warnings

Some antivirus software may flag the `.exe` as suspicious because:
- It's a newly created executable
- PyInstaller executables can trigger false positives

**Solutions:**
1. Add to antivirus exceptions
2. Submit to VirusTotal for analysis
3. Code sign the executable (advanced)

## Testing the Executable

1. **Copy the `.exe` to a clean folder**
```
C:\Test\InGen-YouTube-Downloader.exe
```

2. **Run it** (double-click)

3. **Choose download location** when prompted

4. **Test download** with a YouTube URL

5. **Press F3** to test FFmpeg installation

## Troubleshooting

### Build Fails

**Problem**: PyInstaller errors during build

**Solutions:**
- Update PyInstaller: `pip install --upgrade pyinstaller`
- Check Python version: `python --version` (need 3.8+)
- Run as Administrator
- Disable antivirus temporarily

### .exe Won't Run

**Problem**: Nothing happens when double-clicking

**Solutions:**
- Run from Command Prompt to see errors
- Check Windows Defender / antivirus
- Try running as Administrator
- Ensure on Windows 10/11

### Missing T-Rex Image

**Problem**: No T-Rex image appears in built executable

**Solutions:**
- Check `img/trex.png` exists before building
- Rebuild with `pyinstaller build_exe.spec --clean`
- Image will fall back to 🦖 emoji if missing

### FFmpeg Installation Fails in .exe

**Problem**: Can't install FFmpeg from built executable

**Solutions:**
- Run as Administrator (winget needs admin)
- Check internet connection
- Try manual FFmpeg installation
- Provide FFmpeg installation instructions to users

## Advanced: Custom Icon

To add a custom icon to the `.exe`:

1. Create or download an `.ico` file
2. Place it as `icon.ico` in project folder
3. Edit `build_exe.spec`:
```python
icon='icon.ico'
```
4. Rebuild

## Advanced: Code Signing

To avoid antivirus warnings:

1. Get a code signing certificate
2. Use `signtool` to sign the `.exe`
3. Costs ~$200/year but increases trust

## GitHub Release

To create a release on GitHub:

1. Build the `.exe`
2. Go to your repository
3. Click "Releases" → "Create a new release"
4. Tag: `v1.0.0`
5. Upload `InGen-YouTube-Downloader.exe`
6. Add release notes from CHANGELOG.md
7. Publish!

Users can then download directly from GitHub.

## Size Optimization

To reduce `.exe` size:

### Option 1: Exclude Unused Modules
Edit `build_exe.spec`, add to `excludes`:
```python
excludes=['unittest', 'test', 'distutils'],
```

### Option 2: Use UPX Compression
Already enabled in spec file:
```python
upx=True,
```

### Option 3: One-Folder Build
Change in `build_exe.spec`:
```python
exe = EXE(
    pyz,
    a.scripts,
    # Remove these for folder build:
    # a.binaries,
    # a.zipfiles,
    # a.datas,
    ...
)
```

Creates folder with `.exe` and DLLs (smaller main `.exe`, but multiple files)

## Platform Support

Currently builds for:
- ✅ Windows 10/11 (64-bit)
- ❌ macOS (would need separate build)
- ❌ Linux (would need separate build)

For cross-platform, would need to:
- Build on each OS separately
- Adjust file paths
- Test thoroughly

## Performance

Standalone `.exe` performance:
- **Startup**: Slightly slower than Python script (~2-3 seconds)
- **Runtime**: Same speed as Python script
- **Memory**: Similar usage (~100-200 MB)
- **Downloads**: Full speed, no difference

## Updates

To update the `.exe`:

1. Make changes to `youtube_downloader_gui.py`
2. Update version in CHANGELOG.md
3. Run `build_exe.bat` again
4. Test thoroughly
5. Create new GitHub release

Users need to download new `.exe` for updates.

## Future: Auto-Updater

Possible enhancement:
- Check GitHub for new version on startup
- Download and install updates automatically
- Requires additional code in main script

---

**Ready to build?** Just run `build_exe.bat` and you'll have a standalone executable in minutes!

*"Life finds a way... to compile to .exe"* 🦖



