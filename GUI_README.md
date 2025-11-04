# 🦖 InGen Systems - Isla Nublar YouTube Retrieval Console

## Jurassic Park Themed GUI

A retro-futuristic YouTube downloader inspired by the iconic Jurassic Park computer interfaces from the 1993 film!

---

## 🎨 Design Features

### Visual Style
- **Black background** with **amber/orange** text - classic early 90s terminal aesthetic
- **Green monochrome graphics** for status and progress indicators
- **Retro computer terminal** feel with Courier New font
- **InGen Systems** branding (the fictional company from Jurassic Park)
- **Live feed indicator** in red (like the park monitoring systems)

### Interface Elements

#### Header
- Title: "InGen Systems - Isla Nublar YouTube Retrieval Console"
- Red "LIVE FEED" indicator
- Date stamp showing "04-24-1994" (Jurassic Park movie release date!) with live clock

#### Control Panel
- **<F1> INITIATE** - Start download (also works with F1 key!)
- **CANCEL OPERATION** - Stop download
- **<F2> CHOOSE FORMATS** - Format selection (F2 key shortcut)
- **<F3> SYSTEM DIAGNOSTICS** - Check and install dependencies (F3 key shortcut) ⭐
  - Scans for missing Python packages
  - Automatically installs missing dependencies
  - Shows status in console (no popups!)

#### Information Display
- Dinosaur emoji placeholder (🦖) in green terminal style
- Video information panel showing:
  - Title retrieval status
  - Duration
  - Format
  - All with "OK" confirmations like in the movie

#### Progress System
- **CHARGING...** label (like the park's electric fence systems)
- Green progress bar
- **ENERGY LEVELS** indicator

#### Console Output
- Terminal-style log output
- Amber text on black background
- Shows real-time download progress and status messages

---

## 🚀 How to Use

### Launch the GUI
1. **Easy way:** Double-click `run_gui.bat`
2. **Manual way:** Run `python youtube_downloader_gui.py`

### Download a Video
1. **Enter URL** in the text field at the top
2. **Press F3** (or click the button) to select format and quality
   - Choose from MP4, WEBM, MKV (video)
   - Or MP3, OGG, M4A (audio only)
   - Select quality for videos (1080p, 720p, etc.)
3. **Press F1** (or click INITIATE) to start download
4. Watch the retro console output as your video downloads!
5. Files save to the `downloads/` folder

### Keyboard Shortcuts
- **F1** - Start download
- **F2** - Choose formats
- **F3** - System Diagnostics (check/install dependencies) ⭐

---

## 🎬 Jurassic Park References

- **InGen Systems**: The bioengineering company that created Jurassic Park
- **Isla Nublar**: The island where the park was located
- **04-24-1994**: The original movie's release date
- **DOGFION**: Reference to Lex's "Unix system" scene
- **Amber/Green color scheme**: Matches the film's computer interfaces
- **"LIVE FEED"**: Like the park's security camera system
- **"ENERGY LEVELS"**: References the park's electric fence power system

---

## 📋 Format Options

### Video Formats
- **MP4** - Most compatible, works everywhere
- **WEBM** - Web-optimized format
- **MKV** - High-quality container format

### Audio Formats
- **MP3** - Universal audio format (192 kbps)
- **OGG** - Open-source Vorbis codec
- **M4A** - High-quality AAC audio

### Quality Settings (Video)
- **Best Available** - Highest quality possible
- **1080p** - Full HD
- **720p** - HD
- **480p** - Standard Definition

---

## 🛠️ Technical Details

- Built with **tkinter** (included with Python)
- Uses **yt-dlp** for downloading
- Threading for non-blocking downloads
- Real-time progress updates
- Console logging system

---

## 💡 Tips

- The interface updates in real-time during downloads
- Check the console output (bottom panel) for detailed status
- Progress bar shows download completion percentage
- All downloads automatically save to `downloads/` folder
- Format selection persists between downloads

---

## 🦕 Easter Eggs

Watch for the Jurassic Park references throughout:
- Movie release date in the header
- "DOGFION" button text (Unix system reference)
- InGen Systems branding
- Isla Nublar location
- Retro terminal aesthetic matching the film's computers

---

## 🎭 "Hold onto your butts..."

Enjoy downloading videos with this nostalgic tribute to one of the greatest movies ever made! 

*"Life finds a way... to download YouTube videos."* - Dr. Ian Malcolm (probably)

---

## 📝 Notes

- Requires FFmpeg for audio conversion (MP3, OGG, M4A)
- Virtual environment is automatically activated when using `run_gui.bat`
- Downloads save with original video titles
- The GUI is fully functional - not just for looks!

**"It's a Unix system! I know this!"** 🦖

