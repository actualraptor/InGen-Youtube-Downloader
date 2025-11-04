# 🦖 InGen Systems - YouTube Retrieval Console

<div align="center">

![Jurassic Park Theme](https://img.shields.io/badge/Theme-Jurassic%20Park-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=for-the-badge)

**A retro Jurassic Park themed YouTube downloader with a stunning terminal aesthetic**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots) • [Contributing](#-contributing)

</div>

---

## 📖 Overview

InGen Systems YouTube Retrieval Console is a fully-featured YouTube downloader wrapped in a beautiful Jurassic Park inspired interface. Built with Python and tkinter, it brings the nostalgic amber-on-black terminal aesthetic of the iconic 1993 film to modern video downloading.

### 🎯 Why This Project?

- **Nostalgic UI**: Inspired by the iconic Jurassic Park computer systems
- **Full-Featured**: Download videos in MP4, MP3, or WEBM formats
- **User-Friendly**: Themed GUI with keyboard shortcuts and progress tracking
- **Smart Dependencies**: Automatic dependency checking and installation
- **No Command Line Required**: Everything works through the GUI

---

## ✨ Features

### 🎨 Visual Design
- **Jurassic Park Theme**: Authentic amber/orange and green color scheme
- **Retro Terminal Look**: Courier New font and old-school computer aesthetics
- **Blinking Indicators**: Live feed indicator and status animations
- **Custom Dialogs**: All popups match the Jurassic Park theme

### 🎬 Download Capabilities
- **Multiple Formats**: MP4, MP3, WEBM
- **Quality Selection**: Choose between best, 1080p, 720p, or audio-only
- **Progress Tracking**: Dual progress bars with smooth animations
- **Real-time Console**: Live download status updates

### ⌨️ Keyboard Shortcuts
- **F1**: Initiate Download
- **F2**: Choose Format
- **F3**: System Diagnostics (check if you got all requirements)

### 🔧 Smart Features
- **Auto Dependency Check**: Detects missing packages
- **In-App Installation**: Install yt-dlp, Pillow, and FFmpeg from within the app
- **FFmpeg Integration**: Optional audio conversion support
- **Custom Image Support**: Add your own T-Rex image to the interface

---

## 📦 Installation

### Prerequisites
- **Windows 10/11** (Windows 10 version 1809 or later for winget support)
- **Python 3.8+**

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/actualraptor/InGen-Youtube-Downloader.git
cd InGen-Youtube-Downloader
```

2. **Run the launcher**
```bash
run_gui.bat
```

The launcher will automatically:
- Create a virtual environment
- Install required dependencies
- Launch the GUI

### Manual Installation

If you prefer manual setup:

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the GUI
python youtube_downloader_gui.py
```

---

## 🚀 Usage

### Basic Download

1. Launch the application using `run_gui.bat`
2. Paste a YouTube URL into the input field
3. Press **F1** or click **INITIATE** to start download
4. Watch the Jurassic Park themed progress bars!

### Choosing Format

1. Press **F2** or click **CHOOSE FORMATS**
2. Select your desired format (MP4, MP3, WEBM)
3. Choose quality settings
4. Start your download

### System Diagnostics

1. Press **F3** or click **SYSTEM DIAGNOSTICS**
2. View installed/missing dependencies
3. Install missing packages directly from the GUI
4. Optional: Install FFmpeg for MP3 conversion

### Custom T-Rex Image

Want to personalize your interface?

1. Create an `img` folder in the project directory
2. Add your T-Rex image as `trex.png` (or .jpg, .gif)
3. The app will automatically load it on next launch

---

## 📸 Screenshots

### Main Interface
<img width="1026" height="794" alt="image" src="https://github.com/user-attachments/assets/4aeda213-4f56-4f5b-8993-733ce2a357b8"/>

### Download in Progress
<img width="700" height="78" alt="image" src="https://github.com/user-attachments/assets/ba99a8b3-e857-4570-ac54-792f9ecd2d07"/>

### System Diagnostics
<img width="359" height="106" alt="image" src="https://github.com/user-attachments/assets/2bd6464f-1edc-436c-b490-6790a4f407c0"/>


## 🛠️ Dependencies

### Python Packages
- `yt-dlp` - YouTube download engine
- `Pillow` - Image processing
- `tqdm` - Progress indicators
- `tkinter` - GUI framework (included with Python)

### Optional
- `FFmpeg` - For MP3 conversion (can be installed via the app)

---

## 📝 Configuration

### Download Location
By default, files are saved to `./downloads/`

To change this, modify the download path in the GUI or edit the script.

### Supported Formats

| Format | Requires FFmpeg | Notes |
|--------|----------------|-------|
| MP4 | ❌ No | Works out of the box |
| WEBM | ❌ No | Works out of the box |
| MP3 | ✅ Yes | Requires FFmpeg installation |

---

## 🐛 Troubleshooting

### "yt-dlp not found"
- Press **F3** to run System Diagnostics
- Click "Yes" to install missing dependencies

### "FFmpeg not found" (for MP3)
- Press **F3** to run System Diagnostics
- The app will offer to install FFmpeg via winget
- Alternatively, install manually from [ffmpeg.org](https://ffmpeg.org)

### Downloads fail
1. Check your internet connection
2. Verify the YouTube URL is valid
3. Try a different format (MP4 doesn't require FFmpeg)
4. Run System Diagnostics to check all dependencies

### GUI doesn't start
- Ensure Python 3.8+ is installed
- Try running `python youtube_downloader_gui.py` directly
- Check the console for error messages

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Clone the repo
git clone https://github.com/yourusername/jurassic-youtube-downloader.git

# Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run in development mode
python youtube_downloader_gui.py
```

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Jurassic Park** - For the iconic computer interface inspiration
- **yt-dlp** - For the powerful YouTube download engine
- **Python Community** - For the amazing tools and libraries

---

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/actualraptor/InGen-Youtube-Downloader/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/actualraptor/InGen-Youtube-Downloader/discussions)
- 📧 **Email**: your.email@example.com

---

## ⭐ Star History

If you find this project useful, please consider giving it a star!

---

<div align="center">

**Made with 🦖 and nostalgia**

*"Life finds a way... to download videos."*

</div>




