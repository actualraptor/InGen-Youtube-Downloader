# Developer API Documentation

Documentation for developers who want to understand or extend the codebase.

## Table of Contents
- [Architecture Overview](#architecture-overview)
- [Main Classes](#main-classes)
- [Key Methods](#key-methods)
- [Extending the Application](#extending-the-application)
- [Custom Themes](#custom-themes)

## Architecture Overview

```
youtube_downloader_gui.py
├── JurassicParkDownloader (Main Class)
│   ├── UI Components
│   │   ├── Header (Title, Live Indicator, Clock)
│   │   ├── URL Input
│   │   ├── Control Buttons
│   │   ├── Info Panel (T-Rex, Video Info, Progress)
│   │   └── Console Output
│   ├── Download Engine (yt-dlp integration)
│   ├── Progress Tracking
│   ├── Dependency Management
│   └── Theme System
```

## Main Classes

### JurassicParkDownloader

Main application class that handles all GUI and download functionality.

```python
class JurassicParkDownloader:
    """Main class that creates the Jurassic Park themed YouTube downloader"""
    
    def __init__(self, root):
        # Initialize window, colors, paths, and state
        
    def setup_ui(self):
        # Build all visual elements
        
    def initiate_download(self):
        # Start download process
        
    def download_video(self, url):
        # Actual download logic (runs in thread)
```

## Key Methods

### UI Setup

#### `setup_ui()`
Builds the entire interface including all frames, labels, buttons, and text areas.

```python
def setup_ui(self):
    """Build all the visual elements of the interface"""
    # Creates header, URL input, buttons, panels, console
```

#### `load_trex_image()`
Attempts to load custom T-Rex image, falls back to emoji.

```python
def load_trex_image(self):
    """Try to load T-Rex image from img folder"""
    # Looks for trex.png/jpg/gif in img/ folder
    # Falls back to 🦖 emoji if not found
```

### Animation Methods

#### `start_clock()`
Updates the time display every second.

```python
def start_clock(self):
    """Start updating the clock every second"""
    # Updates clock label with current time
    # Uses Jurassic Park release date as easter egg
```

#### `start_blinking()`
Initiates blinking animations for live indicator and status text.

```python
def start_blinking(self):
    """Start the blinking animations"""
    self.blink_live_indicator()
    self.blink_info_text()
```

#### `blink_live_indicator()`
Toggles the red dot on/off every 500ms.

```python
def blink_live_indicator(self):
    """Make the red LIVE FEED dot blink on and off"""
    if self.blinking_enabled:
        # Toggle between "● LIVE FEED" and "  LIVE FEED"
    self.root.after(500, self.blink_live_indicator)
```

#### `blink_info_text()`
Animates the last dot in "Ready to initialize..."

```python
def blink_info_text(self):
    """Make the last dot in 'Ready to initialize...' blink"""
    if self.blinking_enabled and not self.is_downloading:
        # Toggle between "..." and ".."
    self.root.after(500, self.blink_info_text)
```

### Download Methods

#### `initiate_download()`
Called when user presses F1 or INITIATE button. Validates input and starts download thread.

```python
def initiate_download(self):
    """Called when user clicks F1 or INITIATE button"""
    # Check dependencies
    # Validate URL
    # Start download in separate thread
```

#### `download_video(url)`
Runs in separate thread. Handles actual download using yt-dlp.

```python
def download_video(self, url):
    """This does the actual downloading (runs in a separate thread)"""
    try:
        import yt_dlp
        ydl_opts = self.get_download_options(format_type, quality)
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            ydl.download([url])
    except Exception as e:
        # Error handling
    finally:
        # Reset UI state
```

#### `get_download_options(format_type, quality)`
Returns yt-dlp configuration based on user selections.

```python
def get_download_options(self, format_type, quality):
    """Get yt-dlp options based on format and quality"""
    base_opts = {
        'outtmpl': str(self.download_folder / '%(title)s.%(ext)s'),
        'progress_hooks': [self.progress_hook],
        # ... more options
    }
    # Add format-specific options
    return opts
```

#### `progress_hook(d)`
Callback for yt-dlp progress updates.

```python
def progress_hook(self, d):
    """Handle progress updates from yt-dlp"""
    if d['status'] == 'downloading':
        # Update progress bars
        # Update percentage labels
```

#### `smooth_progress_update(target_percent)`
Animates progress bar smoothly to target percentage.

```python
def smooth_progress_update(self, target_percent):
    """Smoothly animate progress bar to target percentage"""
    # Updates in small increments every 10ms
    # Creates smooth visual animation
```

### Dependency Management

#### `check_dependencies()`
Scans for required Python packages and FFmpeg.

```python
def check_dependencies(self):
    """Check if all the programs we need are installed"""
    # Check yt-dlp, Pillow, tqdm
    # Check FFmpeg
    # Offer installation if missing
```

#### `check_module_installed(module_name)`
Checks if a Python module is available.

```python
def check_module_installed(self, module_name):
    """Check if a Python package is installed"""
    spec = importlib.util.find_spec(module_name)
    return spec is not None
```

#### `install_dependencies()`
Installs missing Python packages via pip.

```python
def install_dependencies(self):
    """Install missing Python dependencies"""
    # Runs pip install in separate thread
    # Updates console with progress
```

#### `install_ffmpeg()`
Installs FFmpeg using winget.

```python
def install_ffmpeg(self):
    """Install FFmpeg using winget"""
    # Runs winget install Gyan.FFmpeg
    # Handles errors and provides alternatives
```

### Dialog Methods

#### `show_themed_dialog(title, message, dialog_type, yes_no, yes_callback)`
Creates custom themed popup dialogs.

```python
def show_themed_dialog(self, title, message, dialog_type="info", 
                       yes_no=False, yes_callback=None):
    """Show a Jurassic Park themed popup window"""
    # Creates Toplevel window
    # Applies JP theme (colors, fonts, borders)
    # Handles Yes/No or OK buttons
```

### Utility Methods

#### `log_console(message)`
Adds a message to the console output area.

```python
def log_console(self, message):
    """Add a message to the console output area"""
    self.console_text.config(state='normal')
    self.console_text.insert('end', message + '\n')
    self.console_text.see('end')
    self.console_text.config(state='disabled')
```

## Extending the Application

### Adding New Format

To add a new download format:

```python
# 1. Add to format selection dialog
def show_format_options(self):
    # Add new radio button
    tk.Radiobutton(format_window,
                   text="NEW FORMAT",
                   variable=self.selected_format,
                   value="newformat",
                   # ... styling
                   ).pack()

# 2. Add format handling
def get_download_options(self, format_type, quality):
    if format_type == 'newformat':
        opts['format'] = 'your_format_spec'
        opts['postprocessors'] = [...]
    return opts
```

### Adding New Keyboard Shortcut

```python
def setup_ui(self):
    # ... existing setup ...
    
    # Add new shortcut
    self.root.bind('<F4>', lambda e: self.your_new_function())
```

### Adding New Feature Button

```python
def setup_ui(self):
    # In button_frame section
    self.btn_new_feature = tk.Button(button_frame,
                                    text="<F4> NEW FEATURE",
                                    font=('Courier New', 12, 'bold'),
                                    bg=self.colors['bg'],
                                    fg=self.colors['amber'],
                                    command=self.new_feature_handler)
    self.btn_new_feature.pack(side='left', padx=5)
```

## Custom Themes

### Color Scheme

The Jurassic Park theme uses:

```python
self.colors = {
    'bg': '#000000',          # Black background
    'amber': '#FF8C00',       # Amber/Orange text
    'green': '#00FF00',       # Bright green for status
    'dark_green': '#003300',  # Dark green background
    'border': '#FF8C00',      # Orange borders
    'red': '#FF0000'          # Red for live indicators
}
```

### Creating a New Theme

```python
class CustomThemeDownloader(JurassicParkDownloader):
    def __init__(self, root):
        super().__init__(root)
        
        # Override colors
        self.colors = {
            'bg': '#YOUR_BG',
            'amber': '#YOUR_PRIMARY',
            'green': '#YOUR_SUCCESS',
            # ... etc
        }
        
        # Rebuild UI with new colors
        self.setup_ui()
```

### Styling Guide

For consistent theming:

1. **Backgrounds**: Always use `self.colors['bg']`
2. **Text**: Use `self.colors['amber']` for labels, `self.colors['green']` for success
3. **Borders**: Use `self.colors['border']` with `highlightthickness=2`
4. **Font**: Stick with Courier New for authenticity
5. **Button Effects**: Use `activebackground` and `activeforeground` for hover

## Threading

Downloads run in separate threads to prevent UI freezing:

```python
thread = threading.Thread(target=self.download_video, args=(url,))
thread.daemon = True  # Dies when main thread dies
thread.start()
```

**Important**: Always update UI from main thread using `self.root.after()`:

```python
# Good
self.root.after(0, lambda: self.log_console("Message"))

# Bad (can cause crashes)
self.log_console("Message")  # Called from worker thread
```

## Event Loop

The application uses tkinter's event loop:

```python
if __name__ == "__main__":
    root = tk.Tk()
    app = JurassicParkDownloader(root)
    root.mainloop()  # Blocks until window closes
```

---

For more examples, see the source code with beginner-friendly comments throughout.




