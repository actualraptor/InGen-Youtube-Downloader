# 🦖 Adding Your Custom T-Rex Image

## Quick Answer

**Put your T-Rex image here:**
```
C:\Scripts\YouTube Downloader\img\
```

**Name it one of these:**
- `trex.png` ⭐ (recommended)
- `trex.jpg`
- `trex.gif`
- `trex_green.png`
- `dinosaur.png`

Then restart the GUI!

---

## Step-by-Step Instructions

### 1. Find or Create Your Image

You can:
- Download a T-Rex silhouette from Google Images
- Use an icon from Flaticon or Icons8
- Create your own in Photoshop/GIMP
- Generate one with AI (DALL-E, Midjourney, etc.)

**Search terms:** "T-Rex silhouette PNG", "dinosaur icon", "T-Rex green terminal"

### 2. Save It With The Right Name

Save your image as:
```
trex.png
```

**Supported formats:**
- PNG (best - supports transparency)
- JPG (also good)
- GIF (works too!)

### 3. Place It In The `img` Folder

```
YouTube Downloader/
├── img/
│   └── trex.png          <-- Your image here!
├── downloads/
├── youtube_downloader_gui.py
└── run_gui.bat
```

### 4. Restart The GUI

Close and reopen the GUI, and your image will appear in the green panel!

---

## Image Specifications

### Ideal Size
- **240x240 pixels** (automatically resized if larger)
- Square or portrait orientation works best

### For Best Jurassic Park Look
✅ High contrast (black on white, or white on black)  
✅ Silhouette style  
✅ Green tinted (optional - can be applied automatically)  
✅ PNG with transparent background  

---

## Automatic Green Tint (Optional)

Want to make ANY image look like a green terminal graphic?

1. Open `youtube_downloader_gui.py` in a text editor
2. Find the `load_trex_image` function (around line 268)
3. Find these lines:
```python
# Convert to green tint for that terminal look (optional)
# Uncomment these lines if you want to force green tint:
# img = img.convert('L')  # Convert to grayscale
# img = ImageOps.colorize(img, black='#001a00', white='#00ff00')
```

4. Remove the `#` from the last two lines to uncomment them:
```python
# Convert to green tint for that terminal look (optional)
# Uncomment these lines if you want to force green tint:
img = img.convert('L')  # Convert to grayscale
img = ImageOps.colorize(img, black='#001a00', white='#00ff00')
```

5. Also add this import at the top of the file (around line 13):
```python
from PIL import Image, ImageTk, ImageOps
```

Now any color image will be converted to that classic green terminal look!

---

## Multiple Name Options

The program looks for images in this order:

1. `trex.png` ⭐
2. `trex.jpg`
3. `trex.gif`
4. `trex_green.png`
5. `dinosaur.png`

It will use the **first one it finds**, so if you want to test different images, just rename them!

---

## Fallback Behavior

If **no image is found**, the GUI will automatically show the 🦖 emoji instead.

So don't worry - the program won't crash if you forget to add an image!

---

## Example Images To Try

### Classic Jurassic Park Style
- T-Rex roaring silhouette (side view)
- T-Rex skeleton
- Jurassic Park logo dinosaur

### Terminal/Retro Style
- Pixelated T-Rex
- ASCII-art style dinosaur
- Green monochrome T-Rex

### Fun Options
- Your favorite dinosaur
- Company logo (why not?)
- Custom pixel art

---

## Testing Your Image

1. Add image to `img/` folder
2. Name it `trex.png`
3. Run `run_gui.bat`
4. Check the green panel on the left!

If it doesn't appear:
- Check the filename is exactly `trex.png`
- Check the file is actually in the `img/` folder
- Check the image format is supported (PNG/JPG/GIF)

---

## Quick Visual Guide

```
📁 YouTube Downloader/
    │
    ├── 📁 img/                     <-- This folder
    │   ├── trex.png                <-- Your image
    │   └── README.txt              <-- Instructions
    │
    ├── 📁 downloads/               (downloaded videos)
    ├── 📄 youtube_downloader_gui.py
    └── 📄 run_gui.bat              <-- Run this
```

---

## Want To Use Different Names?

Edit the code! In `youtube_downloader_gui.py`, find the `load_trex_image` function (line ~247):

```python
image_paths = [
    Path("img/trex.png"),
    Path("img/trex.jpg"),
    Path("img/trex.gif"),
    Path("img/trex_green.png"),
    Path("img/dinosaur.png"),
]
```

Add your own filenames to this list!

---

## 🎬 Ready To Go!

That's it! Drop your T-Rex image in the `img/` folder, name it `trex.png`, and restart the GUI to see it in action!

**"Life finds a way... to display custom images."** 🦖


