================================================================================
                    🦖 T-REX IMAGE FOLDER
================================================================================

This folder is where you place your custom T-Rex or dinosaur image!

📂 LOCATION:
   C:\Scripts\YouTube Downloader\img\


📷 SUPPORTED IMAGE NAMES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The program will automatically look for images in this order:

   1. trex.png
   2. trex.jpg
   3. trex.gif
   4. trex_green.png
   5. dinosaur.png


💡 USAGE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Find or create a T-Rex / dinosaur image
2. Save it with one of the names above (e.g., "trex.png")
3. Place it in THIS folder (img/)
4. Restart the GUI - your image will appear!


🎨 IMAGE RECOMMENDATIONS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

For best Jurassic Park aesthetic:

✓ Square or portrait orientation (240x240px ideal)
✓ PNG format with transparency for best look
✓ Green tinted or monochrome for that terminal vibe
✓ T-Rex silhouette or side profile works great
✓ High contrast images look best


🖼️ FORMATS SUPPORTED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ PNG  (recommended - supports transparency)
✓ JPG  (also works great)
✓ GIF  (static or animated)


🎯 OPTIONAL GREEN TINT:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The code has an optional green tint converter. To enable it:

1. Open: youtube_downloader_gui.py
2. Find the "load_trex_image" function (around line 268)
3. Uncomment these two lines:
   # img = img.convert('L')  # Convert to grayscale
   # img = ImageOps.colorize(img, black='#001a00', white='#00ff00')

This will make ANY image you use look like a green terminal graphic!


🔄 IF NO IMAGE IS FOUND:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Don't worry! The program will automatically show the 🦖 emoji as a fallback.


📝 EXAMPLE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Your file structure should look like:

YouTube Downloader/
├── img/
│   └── trex.png          <-- Your image goes here!
├── downloads/
├── youtube_downloader_gui.py
└── run_gui.bat


🎬 WHERE TO FIND T-REX IMAGES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Google Images: "T-Rex silhouette PNG"
• Icon sites: Flaticon, Icons8, etc.
• Create your own in any image editor
• Use AI to generate one (DALL-E, Midjourney, etc.)


🦕 ENJOY YOUR CUSTOM JURASSIC PARK INTERFACE!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The image will automatically resize to fit the display area (240x240 pixels max).

================================================================================



