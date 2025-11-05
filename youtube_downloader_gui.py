"""
InGen Systems - Isla Nublar YouTube Retrieval Console
Jurassic Park themed YouTube downloader with retro terminal aesthetic
"""

# Import the GUI library (tkinter) for creating windows and buttons
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
# Import threading so downloads dont freeze the GUI
import threading
# Import Path to handle file paths easily
from pathlib import Path
# Import datetime to show the current time in the app
from datetime import datetime
import time
import os
import sys
# Import subprocess to run other programs like pip and winget
import subprocess
# Import importlib to check if modules are installed
import importlib.util
# Import base64 to encode/decode images for storage in config
import base64
# Import io to handle image data in memory
import io


class JurassicParkDownloader:
    """Main class that creates the Jurassic Park themed YouTube downloader"""
    
    def __init__(self, root):
        # Set up the main window
        self.root = root
        self.root.title("InGen Systems - YouTube Retrieval Console")
        self.root.geometry("1024x768")
        self.root.configure(bg='#000000')
        
        # Keep track of missing dependencies so we can install them later
        self.missing_dependencies = []
        self.dependencies_checked = False
        
        # Figure out where this script is located so we can find images and downloads folder
        # When running as exe, use the exe directory, otherwise use script directory
        if getattr(sys, 'frozen', False):
            # Running as compiled exe - use sys._MEIPASS for bundled resources
            self.script_dir = Path(getattr(sys, '_MEIPASS', Path(sys.executable).parent))
            # For persistent config, use the exe's directory, not the temp folder
            self.exe_dir = Path(sys.executable).parent.absolute()
        else:
            # Running as normal Python script
            self.script_dir = Path(__file__).parent.absolute()
            self.exe_dir = self.script_dir
        
        # Define the Jurassic Park color scheme (blacks, oranges, and greens)
        self.colors = {
            'bg': '#000000',          # Black background
            'amber': '#FF8C00',       # Amber/Orange text
            'green': '#00FF00',       # Bright green for status
            'dark_green': '#003300',  # Dark green background
            'border': '#FF8C00',      # Orange borders
            'red': '#FF0000'          # Red for live indicators
        }
        
        # Load or ask for download folder location
        # Config file should be in persistent location (not temp folder)
        self.config_file = self.exe_dir / "config.ini"
        self.download_folder = self.load_download_location()
        self.is_downloading = False
        
        # Track blinking animations
        self.live_blink_state = True
        self.info_blink_state = True
        self.blinking_enabled = True
        
        # Track custom image and GIF animation
        self.custom_image_data = None
        self.gif_frames = []
        self.gif_frame_index = 0
        self.gif_animation_id = None
        self.is_gif = False
        self.hover_button = None
        
        # Build the UI and start the clock
        self.setup_ui()
        self.start_clock()
        self.start_blinking()
        
    def setup_ui(self):
        """Build all the visual elements of the interface"""
        
        # Create the header section at the top with title and live indicator
        header_frame = tk.Frame(self.root, bg=self.colors['bg'], 
                               highlightbackground=self.colors['border'], 
                               highlightthickness=3, bd=5)
        header_frame.pack(fill='x', padx=10, pady=10)
        
        # Main title label
        title_label = tk.Label(header_frame, 
                              text="InGen Systems - Isla Nublar YouTube Retrieval Console",
                              font=('Courier New', 16, 'bold'),
                              bg=self.colors['bg'],
                              fg=self.colors['amber'])
        title_label.pack(side='left', padx=10, pady=5)
        
        # Red live indicator (will blink later)
        self.live_indicator = tk.Label(header_frame,
                                      text="● LIVE FEED",
                                      font=('Courier New', 12, 'bold'),
                                      bg=self.colors['bg'],
                                      fg=self.colors['red'])
        self.live_indicator.pack(side='right', padx=10, pady=5)
        
        # Orange separator line
        separator1 = tk.Frame(self.root, height=2, bg=self.colors['amber'])
        separator1.pack(fill='x', padx=10)
        
        # Clock display in the top right
        clock_frame = tk.Frame(self.root, bg=self.colors['bg'])
        clock_frame.pack(fill='x', padx=10, pady=5)
        
        self.clock_label = tk.Label(clock_frame,
                                   text="",
                                   font=('Courier New', 14),
                                   bg=self.colors['bg'],
                                   fg=self.colors['amber'])
        self.clock_label.pack(side='right', padx=10)
        
        # URL Input Section where user pastes YouTube links
        url_frame = tk.Frame(self.root, bg=self.colors['bg'])
        url_frame.pack(fill='x', padx=15, pady=10)
        
        url_label = tk.Label(url_frame,
                           text="ENTER TARGET URL:",
                           font=('Courier New', 12, 'bold'),
                           bg=self.colors['bg'],
                           fg=self.colors['amber'])
        url_label.pack(anchor='w', pady=(0, 5))
        
        # Text box for URL input (green text on black background)
        self.url_entry = tk.Text(url_frame,
                                height=2,
                                font=('Courier New', 11),
                                bg=self.colors['bg'],
                                fg=self.colors['green'],
                                insertbackground=self.colors['green'],
                                highlightbackground=self.colors['border'],
                                highlightthickness=2,
                                relief='solid')
        self.url_entry.pack(fill='x', pady=5)
        
        # Button row for all controls
        button_frame = tk.Frame(self.root, bg=self.colors['bg'])
        button_frame.pack(fill='x', padx=15, pady=10)
        
        # F1 button to start download
        self.btn_initiate = tk.Button(button_frame,
                                     text="<F1>\nINITIATE",
                                     font=('Courier New', 12, 'bold'),
                                     bg=self.colors['bg'],
                                     fg=self.colors['amber'],
                                     activebackground=self.colors['amber'],
                                     activeforeground=self.colors['bg'],
                                     highlightbackground=self.colors['border'],
                                     highlightthickness=2,
                                     width=15,
                                     height=3,
                                     command=self.initiate_download)
        self.btn_initiate.pack(side='left', padx=5)
        
        # Cancel button (disabled until download starts)
        self.btn_cancel = tk.Button(button_frame,
                                   text="CANCEL\nOPERATION",
                                   font=('Courier New', 12, 'bold'),
                                   bg=self.colors['bg'],
                                   fg=self.colors['amber'],
                                   activebackground=self.colors['amber'],
                                   activeforeground=self.colors['bg'],
                                   highlightbackground=self.colors['border'],
                                   highlightthickness=2,
                                   width=15,
                                   height=3,
                                   command=self.cancel_operation,
                                   state='disabled')
        self.btn_cancel.pack(side='left', padx=5)
        
        # F2 button to pick format (MP4, MP3, WEBM)
        format_label = tk.Button(button_frame,
                                text="<F2> CHOOSE FORMATS",
                                font=('Courier New', 12, 'bold'),
                                bg=self.colors['bg'],
                                fg=self.colors['amber'],
                                highlightbackground=self.colors['border'],
                                highlightthickness=2,
                                width=24,
                                height=3,
                                command=self.show_format_options)
        format_label.pack(side='left', padx=5)
        
        # F3 button to check and install dependencies
        self.btn_check_deps = tk.Button(button_frame,
                                       text="<F3> SYSTEM\nDIAGNOSTICS",
                                       font=('Courier New', 12, 'bold'),
                                       bg=self.colors['bg'],
                                       fg=self.colors['green'],
                                       activebackground=self.colors['green'],
                                       activeforeground=self.colors['bg'],
                                       highlightbackground=self.colors['green'],
                                       highlightthickness=2,
                                       width=20,
                                       height=3,
                                       command=self.check_dependencies)
        self.btn_check_deps.pack(side='left', padx=5)
        
        # F4 button to change download location
        self.btn_change_location = tk.Button(button_frame,
                                            text="<F4> CHANGE\nLOCATION",
                                            font=('Courier New', 12, 'bold'),
                                            bg=self.colors['bg'],
                                            fg=self.colors['amber'],
                                            activebackground=self.colors['amber'],
                                            activeforeground=self.colors['bg'],
                                            highlightbackground=self.colors['border'],
                                            highlightthickness=2,
                                            width=20,
                                            height=3,
                                            command=self.change_download_location)
        self.btn_change_location.pack(side='left', padx=5)
        
        # Main info panel (like the screens in Jurassic Park)
        info_frame = tk.Frame(self.root, bg=self.colors['bg'],
                            highlightbackground=self.colors['border'],
                            highlightthickness=3, bd=5)
        info_frame.pack(fill='both', expand=True, padx=15, pady=10)
        
        # Left panel for T-Rex image
        left_panel = tk.Frame(info_frame, bg=self.colors['dark_green'], width=250)
        left_panel.pack(side='left', fill='y', padx=10, pady=10)
        left_panel.pack_propagate(False)
        
        self.thumbnail_label = tk.Label(left_panel,
                                       bg=self.colors['dark_green'],
                                       cursor='hand2')
        self.thumbnail_label.pack(expand=True)
        
        # Add hover events to show "Change Image" button
        self.thumbnail_label.bind('<Enter>', self.on_image_hover_enter)
        self.thumbnail_label.bind('<Leave>', self.on_image_hover_leave)
        self.thumbnail_label.bind('<Button-1>', lambda e: self.load_custom_image())
        
        # Try to load custom image first, then T-Rex image from img folder (or show dinosaur emoji if not found)
        self.load_trex_image()
        
        # Right panel shows video info and download progress
        right_panel = tk.Frame(info_frame, bg=self.colors['bg'])
        right_panel.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        
        # Info text area (shows video title, duration, etc)
        self.info_text = tk.Text(right_panel,
                                font=('Courier New', 11),
                                bg=self.colors['bg'],
                                fg=self.colors['green'],
                                height=8,
                                relief='flat')
        self.info_text.pack(fill='both', expand=True)
        self.info_text.insert('1.0', "Ready to initialize...")
        self.info_text.config(state='disabled')
        
        # Progress bar inside the info box (shows download percentage)
        progress_info_frame = tk.Frame(right_panel, bg=self.colors['bg'])
        progress_info_frame.pack(fill='x', pady=(10, 0))
        
        tk.Label(progress_info_frame,
                text="DOWNLOAD PROGRESS:",
                font=('Courier New', 9, 'bold'),
                bg=self.colors['bg'],
                fg=self.colors['green']).pack(anchor='w')
        
        # Smooth progress bar (fills up during download)
        self.info_progress_bar = ttk.Progressbar(progress_info_frame,
                                                mode='determinate',
                                                length=400,
                                                style="amber.Horizontal.TProgressbar")
        self.info_progress_bar.pack(fill='x', pady=2)
        
        # Label showing percentage complete
        self.progress_label = tk.Label(progress_info_frame,
                                      text="Ready - 0%",
                                      font=('Courier New', 9),
                                      bg=self.colors['bg'],
                                      fg=self.colors['green'])
        self.progress_label.pack(anchor='w')
        
        # Console output area (like a terminal window)
        console_frame = tk.Frame(self.root, bg=self.colors['bg'],
                               highlightbackground=self.colors['border'],
                               highlightthickness=3, bd=5)
        console_frame.pack(fill='both', expand=True, padx=15, pady=(0, 10))
        
        # Text area for console messages
        self.console_text = tk.Text(console_frame,
                                   font=('Courier New', 10),
                                   bg=self.colors['bg'],
                                   fg=self.colors['amber'],
                                   height=8,
                                   relief='flat')
        self.console_text.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Show initial message
        self.log_console("> Booting up processes...")
        self.log_console("> Analyzing target...")
        self.log_console("> System ready")
        self.log_console(">")
        
        # Variables to store what format the user wants (MP4, MP3, etc)
        self.selected_format = tk.StringVar(value="mp4")
        self.selected_quality = tk.StringVar(value="best")
        
        # Set up keyboard shortcuts (F1, F2, F3)
        self.root.bind('<F1>', lambda e: self.initiate_download())
        self.root.bind('<F2>', lambda e: self.show_format_options())
        self.root.bind('<F3>', lambda e: self.check_dependencies())
        
    def setup_progress_style(self):
        """Set up custom colors for the progress bar"""
        style = ttk.Style()
        style.theme_use('default')
        
        # Info box progress bar is orange/amber
        style.configure("amber.Horizontal.TProgressbar",
                       troughcolor=self.colors['bg'],
                       bordercolor=self.colors['amber'],
                       background=self.colors['amber'],
                       lightcolor=self.colors['amber'],
                       darkcolor=self.colors['amber'])
    
    def scale_image_to_fit(self, img, max_size=(240, 240)):
        """Scale image to fill the box while maintaining aspect ratio"""
        from PIL import Image
        
        # Get target dimensions
        target_width, target_height = max_size
        
        # Get original dimensions
        orig_width, orig_height = img.size
        
        # Calculate scaling factor to fill the box (cover mode)
        # Scale by the larger factor so image fills entire box
        scale_w = target_width / orig_width
        scale_h = target_height / orig_height
        scale = max(scale_w, scale_h)  # Use larger scale to fill box
        
        # Calculate new dimensions
        new_width = int(orig_width * scale)
        new_height = int(orig_height * scale)
        
        # Resize image
        img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Crop to exact size if needed (center crop)
        if new_width > target_width or new_height > target_height:
            left = (new_width - target_width) // 2
            top = (new_height - target_height) // 2
            right = left + target_width
            bottom = top + target_height
            img_resized = img_resized.crop((left, top, right, bottom))
        
        # If image is smaller than target, it will be centered (no padding needed as label handles it)
        return img_resized
    
    def load_trex_image(self):
        """Try to load custom image from config, then T-Rex image from img folder, use emoji if image not found"""
        # Try to import Pillow library for loading images
        try:
            from PIL import Image, ImageTk
        except ImportError:
            # If Pillow not installed, just show a dinosaur emoji
            self.thumbnail_label.config(
                text="🦖",
                font=('Courier New', 80),
                fg=self.colors['green']
            )
            return
        
        # First, try to load custom image from config.ini
        if self.load_custom_image_from_config():
            return  # Custom image loaded successfully
        
        # Stop any GIF animation if running
        self.stop_gif_animation()
        
        # Look for T-Rex image in the img folder
        # When running as .exe, bundled files are in sys._MEIPASS
        if getattr(sys, 'frozen', False):
            # Running as exe - look in bundled resources
            img_folder = Path(getattr(sys, '_MEIPASS', self.script_dir)) / "img"
        else:
            # Running as script
            img_folder = self.script_dir / "img"
        
        image_paths = [
            img_folder / "trex.png",
            img_folder / "trex.jpg",
            img_folder / "trex.gif",
            img_folder / "trex_green.png",
            img_folder / "dinosaur.png",
        ]
        
        # Loop through possible image names and try to load one
        image_found = False
        for image_path in image_paths:
            if image_path.exists():
                try:
                    # Open the image file
                    img = Image.open(image_path)
                    
                    # Check if it's a GIF
                    if img.format == 'GIF' and getattr(img, 'is_animated', False):
                        self.load_gif_animation(image_path)
                        image_found = True
                        break
                    
                    # Scale image to fill the box (240x240)
                    img = self.scale_image_to_fit(img, (240, 240))
                    
                    # You can add a green tint if you want (commented out)
                    # img = img.convert('L')  # Convert to grayscale first
                    # from PIL import ImageOps
                    # img = ImageOps.colorize(img, black='#001a00', white='#00ff00')
                    
                    # Convert to a format tkinter can use and show it
                    self.trex_photo = ImageTk.PhotoImage(img)
                    self.thumbnail_label.config(image=self.trex_photo, text="")
                    
                    image_found = True
                    break
                except Exception as e:
                    # If this image fails, try the next one
                    continue
        
        # If we didnt find any images, just show an emoji
        if not image_found:
            self.thumbnail_label.config(
                text="🦖",
                font=('Courier New', 80),
                fg=self.colors['green']
            )
    
    def on_image_hover_enter(self, event):
        """Show 'Change Image' button when hovering over the image"""
        if self.hover_button is None:
            # Create a button that appears on hover
            self.hover_button = tk.Button(
                self.thumbnail_label,
                text="CHANGE IMAGE",
                font=('Courier New', 9, 'bold'),
                bg=self.colors['amber'],
                fg=self.colors['bg'],
                activebackground=self.colors['green'],
                activeforeground=self.colors['bg'],
                highlightbackground=self.colors['border'],
                highlightthickness=2,
                relief='raised',
                bd=3,
                command=self.load_custom_image
            )
            # Position button at bottom center of image
            self.hover_button.place(relx=0.5, rely=0.95, anchor='s')
    
    def on_image_hover_leave(self, event):
        """Hide 'Change Image' button when mouse leaves the image"""
        if self.hover_button:
            self.hover_button.destroy()
            self.hover_button = None
    
    def load_custom_image(self):
        """Open file dialog to let user select a custom image or GIF"""
        # Stop any existing GIF animation
        self.stop_gif_animation()
        
        # Open file dialog to select image
        file_path = filedialog.askopenfilename(
            title="Select Custom Image or GIF",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"),
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg *.jpeg"),
                ("GIF files", "*.gif"),
                ("All files", "*.*")
            ]
        )
        
        if not file_path:
            return  # User cancelled
        
        try:
            from PIL import Image, ImageTk
            
            # Open the image to check if it's valid
            img = Image.open(file_path)
            
            # Check if it's an animated GIF
            if img.format == 'GIF' and getattr(img, 'is_animated', False):
                # Load and animate the GIF
                self.load_gif_animation(Path(file_path))
                # Save GIF to config
                self.save_custom_image_to_config(Path(file_path))
            else:
                # Load static image - scale to fill box
                img = self.scale_image_to_fit(img, (240, 240))
                self.trex_photo = ImageTk.PhotoImage(img)
                self.thumbnail_label.config(image=self.trex_photo, text="")
                self.is_gif = False
                
                # Save image to config as base64
                self.save_custom_image_to_config(Path(file_path))
            
            self.log_console(f"> Custom image loaded: {Path(file_path).name}")
            
        except Exception as e:
            self.show_themed_dialog(
                "Error",
                f"Failed to load image:\n{str(e)}",
                yes_no=False
            )
    
    def load_custom_image_from_config(self):
        """Load custom image from config.ini if it exists"""
        try:
            from PIL import Image, ImageTk
            
            if not self.config_file.exists():
                return False
            
            # Read config file
            custom_image_base64 = None
            is_gif_flag = False
            
            with open(self.config_file, 'r') as f:
                for line in f:
                    if line.startswith('custom_image_data='):
                        custom_image_base64 = line.split('=', 1)[1].strip()
                    elif line.startswith('custom_image_is_gif='):
                        is_gif_flag = line.split('=', 1)[1].strip().lower() == 'true'
            
            if not custom_image_base64:
                return False
            
            # Decode base64 image data
            image_data = base64.b64decode(custom_image_base64)
            image_bytes = io.BytesIO(image_data)
            
            # Load image from bytes
            img = Image.open(image_bytes)
            
            if is_gif_flag and getattr(img, 'is_animated', False):
                # For GIFs, we need to save temporarily and reload (or use BytesIO properly)
                # Actually, let's reload from the bytes directly
                image_bytes.seek(0)  # Reset to beginning
                self.load_gif_from_bytes(image_bytes)
                return True
            else:
                # Static image - scale to fill box
                img = self.scale_image_to_fit(img, (240, 240))
                self.trex_photo = ImageTk.PhotoImage(img)
                self.thumbnail_label.config(image=self.trex_photo, text="")
                self.is_gif = False
                return True
                
        except Exception as e:
            # If loading fails, just use default image
            return False
    
    def save_custom_image_to_config(self, image_path):
        """Save custom image to config.ini as base64 encoded data"""
        try:
            from PIL import Image
            
            # Read image file and encode as base64
            with open(image_path, 'rb') as f:
                image_data = base64.b64encode(f.read()).decode('utf-8')
            
            # Check if it's actually an animated GIF
            is_gif = False
            try:
                img_check = Image.open(image_path)
                is_gif = (img_check.format == 'GIF' and getattr(img_check, 'is_animated', False))
                img_check.close()
            except:
                pass
            
            # Read existing config
            config_lines = []
            if self.config_file.exists():
                with open(self.config_file, 'r') as f:
                    config_lines = f.readlines()
            
            # Remove old custom_image lines if they exist
            config_lines = [line for line in config_lines 
                          if not line.startswith('custom_image_data=') 
                          and not line.startswith('custom_image_is_gif=')]
            
            # Add new custom image data
            config_lines.append(f'custom_image_data={image_data}\n')
            config_lines.append(f'custom_image_is_gif={str(is_gif).lower()}\n')
            
            # Write back to config file
            with open(self.config_file, 'w') as f:
                f.writelines(config_lines)
                
        except Exception as e:
            self.log_console(f"> Warning: Could not save custom image to config: {str(e)}")
    
    def load_gif_animation(self, gif_path):
        """Load a GIF file and set up animation"""
        try:
            from PIL import Image, ImageTk
            
            # Open GIF
            img = Image.open(gif_path)
            
            if not getattr(img, 'is_animated', False):
                # Not animated, treat as static image - scale to fill box
                img = self.scale_image_to_fit(img, (240, 240))
                self.trex_photo = ImageTk.PhotoImage(img)
                self.thumbnail_label.config(image=self.trex_photo, text="")
                self.is_gif = False
                return
            
            # Extract all frames
            self.gif_frames = []
            self.gif_frame_index = 0
            self.is_gif = True
            
            try:
                frame_num = 0
                while True:
                    # Resize frame to fill panel
                    frame = img.copy()
                    frame = self.scale_image_to_fit(frame, (240, 240))
                    frame_photo = ImageTk.PhotoImage(frame)
                    
                    # Get duration for this frame (default to 100ms if not specified)
                    duration = img.info.get('duration', 100)
                    if duration == 0:
                        duration = 100  # Prevent division by zero
                    
                    self.gif_frames.append((frame_photo, duration))
                    
                    frame_num += 1
                    try:
                        img.seek(frame_num)
                    except EOFError:
                        break
                        
            except Exception as e:
                # If frame extraction fails, just use first frame as static
                img.seek(0)
                img = self.scale_image_to_fit(img, (240, 240))
                self.trex_photo = ImageTk.PhotoImage(img)
                self.thumbnail_label.config(image=self.trex_photo, text="")
                self.is_gif = False
                return
            
            # Start animation
            if self.gif_frames:
                self.animate_gif()
                
        except Exception as e:
            # If GIF loading fails, just show error
            self.log_console(f"> Error loading GIF: {str(e)}")
    
    def load_gif_from_bytes(self, image_bytes):
        """Load GIF animation from bytes (for config loading)"""
        try:
            from PIL import Image, ImageTk
            
            img = Image.open(image_bytes)
            
            if not getattr(img, 'is_animated', False):
                # Not animated - scale to fill box
                img = self.scale_image_to_fit(img, (240, 240))
                self.trex_photo = ImageTk.PhotoImage(img)
                self.thumbnail_label.config(image=self.trex_photo, text="")
                self.is_gif = False
                return
            
            # Extract frames
            self.gif_frames = []
            self.gif_frame_index = 0
            self.is_gif = True
            
            try:
                frame_num = 0
                while True:
                    frame = img.copy()
                    frame = self.scale_image_to_fit(frame, (240, 240))
                    frame_photo = ImageTk.PhotoImage(frame)
                    
                    # Get duration for this frame (default to 100ms if not specified)
                    duration = img.info.get('duration', 100)
                    if duration == 0:
                        duration = 100  # Prevent division by zero
                    
                    self.gif_frames.append((frame_photo, duration))
                    
                    frame_num += 1
                    try:
                        img.seek(frame_num)
                    except EOFError:
                        break
                        
            except Exception as e:
                # Fallback to first frame
                img.seek(0)
                img = self.scale_image_to_fit(img, (240, 240))
                self.trex_photo = ImageTk.PhotoImage(img)
                self.thumbnail_label.config(image=self.trex_photo, text="")
                self.is_gif = False
                return
            
            # Start animation
            if self.gif_frames:
                self.animate_gif()
                
        except Exception as e:
            self.log_console(f"> Error loading GIF from config: {str(e)}")
    
    def animate_gif(self):
        """Animate GIF frames by cycling through them"""
        if not self.is_gif or not self.gif_frames:
            return
        
        # Get current frame
        frame_photo, duration = self.gif_frames[self.gif_frame_index]
        
        # Update image
        self.thumbnail_label.config(image=frame_photo)
        self.trex_photo = frame_photo  # Keep reference to prevent garbage collection
        
        # Move to next frame (loop back to start)
        self.gif_frame_index = (self.gif_frame_index + 1) % len(self.gif_frames)
        
        # Schedule next frame (duration is in milliseconds)
        self.gif_animation_id = self.root.after(duration, self.animate_gif)
    
    def stop_gif_animation(self):
        """Stop any running GIF animation"""
        if self.gif_animation_id:
            self.root.after_cancel(self.gif_animation_id)
            self.gif_animation_id = None
        self.is_gif = False
        self.gif_frames = []
        self.gif_frame_index = 0
    
    def load_download_location(self):
        """Load download location from config or ask user"""
        # Try to load from config file
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    for line in f:
                        if line.startswith('download_path='):
                            path = Path(line.split('=', 1)[1].strip())
                            if path.exists():
                                return path
            except:
                pass
        
        # Ask user for download location on first run using themed dialog
        # Store the result to check what they clicked
        result = {"response": None}
        
        def on_yes():
            result["response"] = True
        
        def on_no():
            result["response"] = False
        
        # Show the dialog and WAIT for user to click a button
        self.show_themed_dialog(
            "FIRST TIME INITIALIZATION",
            ">>> InGen Systems - Isla Nublar Console <<<\n\n"
            "This appears to be your first time running this system.\n\n"
            "Would you like to specify a download location?\n\n"
            "YES: Choose custom folder\n"
            "NO: Use default location (next to .exe)",
            dialog_type="info",
            yes_no=True,
            yes_callback=on_yes,
            no_callback=on_no,
            wait=True  # Wait for dialog to close before continuing
        )
        
        response = result["response"]
        
        if response:
            from tkinter import filedialog
            chosen_path = filedialog.askdirectory(
                title="Choose Download Folder",
                initialdir=str(Path.home() / "Downloads")
            )
            if chosen_path:
                download_path = Path(chosen_path)
            else:
                download_path = self.exe_dir / "downloads"
        else:
            download_path = self.exe_dir / "downloads"
        
        # Create folder if it doesnt exist
        download_path.mkdir(parents=True, exist_ok=True)
        
        # Save to config
        try:
            with open(self.config_file, 'w') as f:
                f.write(f'download_path={download_path}\n')
        except:
            pass
        
        return download_path
    
    def change_download_location(self):
        """Allow user to change download location"""
        from tkinter import filedialog
        new_path = filedialog.askdirectory(
            title="Choose New Download Folder",
            initialdir=str(self.download_folder)
        )
        
        if new_path:
            self.download_folder = Path(new_path)
            self.download_folder.mkdir(parents=True, exist_ok=True)
            
            # Save to config
            try:
                with open(self.config_file, 'w') as f:
                    f.write(f'download_path={self.download_folder}\n')
            except:
                pass
            
            self.log_console(f"> Download location changed to: {self.download_folder}")
            self.show_themed_dialog(
                "Location Updated",
                f"Downloads will now be saved to:\n{self.download_folder}",
                dialog_type="info"
            )
    
    def start_clock(self):
        """Start updating the clock every second"""
        def update_clock():
            # Show current time (date is fixed to Jurassic Park release date as easter egg)
            current_time = datetime.now().strftime("%H:%M:%S")
            self.clock_label.config(text=f"11-06-1993 {current_time}")
            self.root.after(1000, update_clock)
        update_clock()
    
    def start_blinking(self):
        """Start the blinking animations for live indicator and info text"""
        self.blink_live_indicator()
        self.blink_info_text()
    
    def blink_live_indicator(self):
        """Make the red LIVE FEED dot blink on and off"""
        if self.blinking_enabled:
            if self.live_blink_state:
                self.live_indicator.config(text="● LIVE FEED")
            else:
                self.live_indicator.config(text="  LIVE FEED")  # Just spaces, no dot
            self.live_blink_state = not self.live_blink_state
        else:
            # When not blinking, keep it solid
            self.live_indicator.config(text="● LIVE FEED")
        
        # Repeat every 500ms (twice per second)
        self.root.after(500, self.blink_live_indicator)
    
    def blink_info_text(self):
        """Make the last dot in 'Ready to initialize...' blink"""
        if self.blinking_enabled and not self.is_downloading:
            if self.info_blink_state:
                text = "Ready to initialize..."
            else:
                text = "Ready to initialize.."
            
            self.info_text.config(state='normal')
            self.info_text.delete('1.0', 'end')
            self.info_text.insert('1.0', text)
            self.info_text.config(state='disabled')
            
            self.info_blink_state = not self.info_blink_state
        
        # Repeat every 500ms
        self.root.after(500, self.blink_info_text)
    
    def log_console(self, message):
        """Add a message to the console output area"""
        self.console_text.config(state='normal')
        self.console_text.insert('end', message + '\n')
        self.console_text.see('end')
        self.console_text.config(state='disabled')
        self.root.update()
    
    def show_format_options(self):
        """Show format selection dialog"""
        format_window = tk.Toplevel(self.root)
        format_window.title("Configuration - Format Selection")
        format_window.configure(bg=self.colors['bg'])
        # Don't set fixed size - let it size naturally, then fit to content
        
        tk.Label(format_window,
                text="SELECT OUTPUT FORMAT",
                font=('Courier New', 14, 'bold'),
                bg=self.colors['bg'],
                fg=self.colors['amber']).pack(pady=10)
        
        # Format options - Simplified to 3 main formats
        formats = [
            ("MP4 (Video - Recommended)", "mp4"),
            ("MP3 (Audio Only - Requires FFmpeg)", "mp3"),
            ("WEBM (Video - Alternative)", "webm"),
        ]
        
        for text, value in formats:
            tk.Radiobutton(format_window,
                          text=text,
                          variable=self.selected_format,
                          value=value,
                          font=('Courier New', 11),
                          bg=self.colors['bg'],
                          fg=self.colors['green'],
                          selectcolor=self.colors['dark_green'],
                          activebackground=self.colors['bg'],
                          activeforeground=self.colors['amber']).pack(anchor='w', padx=20, pady=5)
        
        tk.Label(format_window,
                text="SELECT QUALITY (Video Only)",
                font=('Courier New', 14, 'bold'),
                bg=self.colors['bg'],
                fg=self.colors['amber']).pack(pady=10)
        
        qualities = [
            ("Best Available", "best"),
            ("1080p (Full HD)", "1080p"),
            ("720p (HD)", "720p"),
            ("480p (SD)", "480p")
        ]
        
        for text, value in qualities:
            tk.Radiobutton(format_window,
                          text=text,
                          variable=self.selected_quality,
                          value=value,
                          font=('Courier New', 11),
                          bg=self.colors['bg'],
                          fg=self.colors['green'],
                          selectcolor=self.colors['dark_green'],
                          activebackground=self.colors['bg'],
                          activeforeground=self.colors['amber']).pack(anchor='w', padx=20, pady=5)
        
        tk.Button(format_window,
                 text="CONFIRM SELECTION",
                 font=('Courier New', 12, 'bold'),
                 bg=self.colors['bg'],
                 fg=self.colors['amber'],
                 highlightbackground=self.colors['border'],
                 highlightthickness=2,
                 command=format_window.destroy).pack(pady=20)
        
        # Update the window to calculate actual size needed, then set it properly
        format_window.update_idletasks()
        # Get the required size and add some padding
        width = format_window.winfo_reqwidth() + 40
        height = format_window.winfo_reqheight() + 40
        format_window.geometry(f"{width}x{height}")
        # Center the window on screen
        format_window.update_idletasks()
        x = (format_window.winfo_screenwidth() // 2) - (format_window.winfo_width() // 2)
        y = (format_window.winfo_screenheight() // 2) - (format_window.winfo_height() // 2)
        format_window.geometry(f"{width}x{height}+{x}+{y}")
    
    def initiate_download(self):
        """Called when user clicks F1 or INITIATE button"""
        # First check if yt-dlp is installed (we need it to download videos)
        if not self.check_module_installed('yt_dlp'):
            self.show_themed_dialog(
                "Missing Dependency",
                "⚠️ YouTube Downloader Engine (yt-dlp) is not installed!\n\n"
                "Would you like to run System Diagnostics to check and install dependencies?",
                dialog_type="warning",
                yes_no=True,
                yes_callback=self.check_dependencies
            )
            return
        
        # Get the URL from the text box
        url = self.url_entry.get('1.0', 'end-1c').strip()
        
        # Check if user actually entered a URL
        if not url:
            self.show_themed_dialog("Warning", "Please enter a YouTube URL!", dialog_type="warning")
            return
        
        # Make sure we're not already downloading something
        if self.is_downloading:
            self.show_themed_dialog("Info", "Download already in progress!", dialog_type="info")
            return
        
        # Set flags and disable the initiate button
        self.is_downloading = True
        self.blinking_enabled = False  # Stop blinking during download
        self.btn_initiate.config(state='disabled')
        self.btn_cancel.config(state='normal')
        
        # Update info text to show we're downloading
        self.info_text.config(state='normal')
        self.info_text.delete('1.0', 'end')
        self.info_text.insert('1.0', "Initializing download...")
        self.info_text.config(state='disabled')
        
        # Log what we're about to do
        self.log_console("> Download initiated...")
        self.log_console(f"> Target URL: {url[:50]}...")
        self.log_console(f"> Format: {self.selected_format.get().upper()}")
        self.log_console(f"> Quality: {self.selected_quality.get()}")
        self.log_console("> Connecting to target...")
        
        # Start download in a separate thread so the GUI doesnt freeze
        thread = threading.Thread(target=self.download_video, args=(url,))
        thread.daemon = True
        thread.start()
    
    def cancel_operation(self):
        """Called when user clicks CANCEL OPERATION button"""
        self.is_downloading = False
        self.blinking_enabled = True  # Resume blinking
        self.btn_initiate.config(state='normal')
        self.btn_cancel.config(state='disabled')
        
        # Reset info text back to ready state
        self.info_text.config(state='normal')
        self.info_text.delete('1.0', 'end')
        self.info_text.insert('1.0', "Ready to initialize...")
        self.info_text.config(state='disabled')
        
        self.log_console("> Operation cancelled by user")
    
    def download_video(self, url):
        """This does the actual downloading (runs in a separate thread)"""
        try:
            # Load yt-dlp library
            import yt_dlp
            
            format_type = self.selected_format.get()
            quality = self.selected_quality.get()
            
            ydl_opts = self.get_download_options(format_type, quality)
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                self.log_console("> Retrieving video information...")
                
                info = ydl.extract_info(url, download=False)
                title = info.get('title', 'Unknown')
                duration = info.get('duration', 0)
                
                # Update info display
                self.info_text.config(state='normal')
                self.info_text.delete('1.0', 'end')
                self.info_text.insert('1.0', 
                    f"Retrieving Title... OK\n"
                    f"{title}.. OK\n"
                    f"Duration... {duration//60}:{duration%60:02d}.. OK\n"
                    f"Format... {format_type.upper()}")
                self.info_text.config(state='disabled')
                
                self.log_console(f"> Title: {title}")
                self.log_console("> Initiating download sequence...")
                self.log_console("> ")
                
                # Reset progress tracking
                self._last_percent = -1
                
                # Download
                ydl.download([url])
                
                self.log_console("> ")
                self.log_console("> ====================================")
                self.log_console("> DOWNLOAD COMPLETE")
                self.log_console("> ====================================")
                self.log_console(f"> File saved to: {self.download_folder}/")
                self.log_console("> Operation successful")
                self.log_console(">")
                
        except Exception as e:
            error_msg = str(e)
            self.log_console("> ====================================")
            self.log_console("> ERROR: DOWNLOAD FAILED")
            self.log_console("> ====================================")
            self.log_console(f"> {error_msg}")
            self.log_console("> ")
            
            # Check for FFmpeg error
            if 'ffmpeg' in error_msg.lower() or 'ffprobe' in error_msg.lower():
                self.log_console("> CRITICAL: FFmpeg not found")
                self.log_console("> FFmpeg is required for audio conversion")
                self.log_console("> ")
                self.log_console("> To install FFmpeg:")
                self.log_console(">   1. Run: winget install ffmpeg")
                self.log_console(">   OR")
                self.log_console(">   2. Download from: https://ffmpeg.org")
                self.log_console("> ")
                self.log_console("> TIP: Use MP4 format (no FFmpeg needed)")
                self.log_console("> ")
                
                self.show_themed_dialog(
                    "FFmpeg Required",
                    "✗ Audio conversion requires FFmpeg!\n\n"
                    "To install:\n"
                    "• Run: winget install ffmpeg\n"
                    "• Or download from: https://ffmpeg.org\n\n"
                    "Tip: MP4 downloads work without FFmpeg",
                    dialog_type="error"
                )
            else:
                self.show_themed_dialog(
                    "Download Error",
                    f"✗ Download failed:\n\n{error_msg}",
                    dialog_type="error"
                )
        
        finally:
            self.is_downloading = False
            self.blinking_enabled = True  # Resume blinking after download
            self.btn_initiate.config(state='normal')
            self.btn_cancel.config(state='disabled')
            self._last_percent = -1
            
            # Reset info text back to ready state with blinking dot
            self.info_text.config(state='normal')
            self.info_text.delete('1.0', 'end')
            self.info_text.insert('1.0', "Ready to initialize...")
            self.info_text.config(state='disabled')
    
    def get_download_options(self, format_type, quality):
        """Get yt-dlp options based on format and quality"""
        base_opts = {
            'outtmpl': str(self.download_folder / '%(title)s.%(ext)s'),
            'progress_hooks': [self.progress_hook],
        }
        
        # Try to find FFmpeg automatically
        try:
            result = subprocess.run(['where', 'ffmpeg'], capture_output=True, text=True)
            if result.returncode == 0:
                ffmpeg_path = result.stdout.strip().split('\n')[0]
                ffmpeg_dir = str(Path(ffmpeg_path).parent)
                base_opts['ffmpeg_location'] = ffmpeg_dir
        except:
            pass
        
        # Check FFmpeg availability
        ffmpeg_available = False
        try:
            result = subprocess.run(['where', 'ffmpeg'], capture_output=True, text=True, timeout=2)
            ffmpeg_available = (result.returncode == 0)
        except:
            pass
        
        # Format-specific options
        if format_type == 'mp3':
            # MP3 requires FFmpeg for audio extraction
            if not ffmpeg_available:
                raise Exception("FFmpeg is required for MP3 conversion. Install it with: winget install ffmpeg")
            
            base_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        
        elif format_type == 'mp4':
            # MP4 - Works with or without FFmpeg
            # Prioritize formats that don't need merging
            if quality == 'best':
                # Get best pre-merged MP4 format (no FFmpeg needed)
                base_opts['format'] = 'best[ext=mp4]/bestvideo[ext=mp4]+bestaudio[ext=m4a]/best'
            else:
                height = quality.replace('p', '')
                base_opts['format'] = f'best[height<={height}][ext=mp4]/bestvideo[height<={height}][ext=mp4]+bestaudio[ext=m4a]/best'
            
            # Only set merge format if we have FFmpeg
            if ffmpeg_available:
                base_opts['merge_output_format'] = 'mp4'
        
        elif format_type == 'webm':
            # WEBM - Works with or without FFmpeg
            if quality == 'best':
                base_opts['format'] = 'best[ext=webm]/bestvideo[ext=webm]+bestaudio[ext=webm]/best'
            else:
                height = quality.replace('p', '')
                base_opts['format'] = f'best[height<={height}][ext=webm]/bestvideo[height<={height}][ext=webm]+bestaudio[ext=webm]/best'
            
            if ffmpeg_available:
                base_opts['merge_output_format'] = 'webm'
        
        return base_opts
    
    def smooth_progress_update(self, target_percent, downloaded_mb, total_mb, speed_mb):
        """Smoothly update progress bar"""
        current = self.info_progress_bar['value']
        
        # Smooth transition to target
        if current < target_percent:
            step = min(0.5, target_percent - current)
            new_value = current + step
            self.info_progress_bar['value'] = new_value
            
            # Update label with smooth percentage
            self.progress_label.config(
                text=f"{new_value:.1f}% - {downloaded_mb:.1f}MB / {total_mb:.1f}MB @ {speed_mb:.1f}MB/s"
            )
            
            # Schedule next update for smooth animation
            if new_value < target_percent:
                self.root.after(10, lambda: self.smooth_progress_update(target_percent, downloaded_mb, total_mb, speed_mb))
        else:
            # Final update when we reach target
            self.info_progress_bar['value'] = target_percent
            self.progress_label.config(
                text=f"{target_percent:.1f}% - {downloaded_mb:.1f}MB / {total_mb:.1f}MB @ {speed_mb:.1f}MB/s"
            )
    
    def progress_hook(self, d):
        """Update progress bar during download"""
        if d['status'] == 'downloading':
            # Try different progress indicators
            if 'downloaded_bytes' in d and 'total_bytes' in d:
                percent = (d['downloaded_bytes'] / d['total_bytes']) * 100
                
                # Update console with progress
                downloaded_mb = d['downloaded_bytes'] / (1024 * 1024)
                total_mb = d['total_bytes'] / (1024 * 1024)
                speed = d.get('speed', 0)
                speed_mb = speed / (1024 * 1024) if speed else 0
                
                # Smooth progress update
                self.smooth_progress_update(percent, downloaded_mb, total_mb, speed_mb)
                
                # Only log every 10% to avoid spam
                if int(percent) % 10 == 0 and int(percent) != getattr(self, '_last_percent', -1):
                    self.log_console(f"> Progress: {percent:.0f}% ({downloaded_mb:.1f}MB / {total_mb:.1f}MB) @ {speed_mb:.1f}MB/s")
                    self._last_percent = int(percent)
                
                self.root.update_idletasks()
            elif 'total_bytes_estimate' in d:
                percent = (d['downloaded_bytes'] / d['total_bytes_estimate']) * 100
                downloaded_mb = d['downloaded_bytes'] / (1024 * 1024)
                total_mb = d['total_bytes_estimate'] / (1024 * 1024)
                speed = d.get('speed', 0)
                speed_mb = speed / (1024 * 1024) if speed else 0
                self.smooth_progress_update(percent, downloaded_mb, total_mb, speed_mb)
                self.root.update_idletasks()
        elif d['status'] == 'finished':
            self.info_progress_bar['value'] = 100
            self.progress_label.config(text="100.0% - Complete - Processing file...")
            self._last_percent = -1
            self.log_console("> Download complete, processing file...")
        elif d['status'] == 'error':
            self.log_console("> ERROR during download")
            self.info_progress_bar['value'] = 0
            self.progress_label.config(text="0% - Error")
    
    def check_module_installed(self, module_name, package_name=None):
        """Check if a Python package is installed on this computer"""
        if package_name is None:
            package_name = module_name
        
        # Try to find the module and return True if found, False if not found
        spec = importlib.util.find_spec(module_name)
        return spec is not None
    
    def check_ffmpeg_installed(self):
        """Check if FFmpeg is installed on this computer"""
        try:
            # Run the 'where ffmpeg' command to see if FFmpeg is in the PATH
            result = subprocess.run(['where', 'ffmpeg'], capture_output=True, text=True, timeout=2)
            return result.returncode == 0
        except:
            return False
    
    def check_dependencies(self):
        """Check if all the programs we need are installed (called when F3 is pressed)"""
        self.log_console("> ====================================")
        self.log_console("> SYSTEM DIAGNOSTICS INITIATED")
        self.log_console("> ====================================")
        self.log_console("> Scanning system modules...")
        self.log_console("> ")
        
        # List of Python packages we need to download videos
        required_deps = [
            ('yt_dlp', 'yt-dlp', 'YouTube Downloader Engine'),
            ('PIL', 'Pillow', 'Image Processing System'),
            ('tqdm', 'tqdm', 'Progress Indicator'),
        ]
        
        self.missing_dependencies = []
        all_installed = True
        
        # Loop through each package and check if it's installed
        for module_name, package_name, description in required_deps:
            self.log_console(f"> Checking {description}...")
            if self.check_module_installed(module_name):
                self.log_console(f">   [{module_name}] .............. OK")
            else:
                self.log_console(f">   [{module_name}] .............. MISSING!")
                self.missing_dependencies.append((module_name, package_name, description))
                all_installed = False
        
        # Check if FFmpeg is installed (needed for MP3 conversion)
        self.log_console(f"> Checking FFmpeg (Audio Converter)...")
        ffmpeg_installed = self.check_ffmpeg_installed()
        if ffmpeg_installed:
            self.log_console(f">   [ffmpeg] .............. OK")
        else:
            self.log_console(f">   [ffmpeg] .............. MISSING!")
            self.log_console(">   (Optional: Required for MP3 conversion)")
            self.missing_dependencies.append(('ffmpeg', 'ffmpeg', 'FFmpeg Audio Converter'))
            # FFmpeg is optional so we dont treat this as a critical error
        
        self.log_console("> ")
        self.log_console("> ====================================")
        
        if all_installed and ffmpeg_installed:
            self.log_console("> STATUS: ALL SYSTEMS OPERATIONAL")
            self.log_console("> ====================================")
            self.log_console("> All dependencies installed")
            self.log_console("> Ready to retrieve videos")
            self.log_console("> ")
        elif all_installed and not ffmpeg_installed:
            self.log_console("> STATUS: SYSTEMS OPERATIONAL (MP3 UNAVAILABLE)")
            self.log_console("> ====================================")
            self.log_console("> Python modules installed")
            self.log_console("> FFmpeg missing - MP3 conversion unavailable")
            self.log_console("> MP4 and WEBM downloads will work fine")
            self.log_console("> ")
            
            # Show themed FFmpeg dialog
            self.show_ffmpeg_install_dialog()
        else:
            self.log_console(f"> STATUS: {len(self.missing_dependencies)} CRITICAL MODULES MISSING")
            self.log_console("> ====================================")
            self.log_console("> ")
            
            missing_list = "\n".join([f"• {desc} ({pkg})" 
                                    for _, pkg, desc in self.missing_dependencies])
            
            self.show_themed_dialog(
                "System Diagnostics - Missing Dependencies",
                f"⚠️ CRITICAL MODULES MISSING!\n\n"
                f"The following modules are required:\n\n{missing_list}\n\n"
                f"Would you like to install them now?\n\n"
                f"(This will run: pip install <packages>)",
                dialog_type="warning",
                yes_no=True,
                yes_callback=self.install_dependencies
            )
        
        self.dependencies_checked = True
    
    def show_themed_dialog(self, title, message, dialog_type="info", yes_no=False, yes_callback=None, no_callback=None, wait=False):
        """Show a Jurassic Park themed popup window instead of ugly Windows dialogs"""
        # Create a new popup window
        dialog = tk.Toplevel(self.root)
        dialog.title(title)
        dialog.geometry("600x400")  # Made taller so buttons are more visible
        dialog.configure(bg=self.colors['bg'])
        dialog.transient(self.root)
        dialog.grab_set()
        
        # Pick the right icon and color based on message type
        icons = {
            "error": ("✗", self.colors['red']),
            "warning": ("⚠", self.colors['amber']),
            "info": ("ℹ", self.colors['green'])
        }
        icon, color = icons.get(dialog_type, ("ℹ", self.colors['green']))
        
        # Create header section with title
        header_frame = tk.Frame(dialog, bg=self.colors['bg'], 
                               highlightbackground=color,
                               highlightthickness=2, bd=3)
        header_frame.pack(fill='x', padx=10, pady=10)
        
        tk.Label(header_frame,
                text=f"{icon} {title}",
                font=('Courier New', 14, 'bold'),
                bg=self.colors['bg'],
                fg=color).pack(pady=10)
        
        # Create message area
        content_frame = tk.Frame(dialog, bg=self.colors['bg'])
        content_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        tk.Label(content_frame,
                text=message,
                font=('Courier New', 10),
                bg=self.colors['bg'],
                fg=self.colors['green'],
                justify='left',
                wraplength=550).pack(anchor='w', pady=20)
        
        # Create button area
        button_frame = tk.Frame(dialog, bg=self.colors['bg'])
        button_frame.pack(fill='x', padx=20, pady=20)
        
        if yes_no:
            def on_yes_click():
                dialog.destroy()
                if yes_callback:
                    yes_callback()
            
            def on_no_click():
                dialog.destroy()
                if no_callback:
                    no_callback()
            
            tk.Button(button_frame,
                     text="YES",
                     font=('Courier New', 12, 'bold'),
                     bg=self.colors['bg'],
                     fg=self.colors['green'],
                     activebackground=self.colors['green'],
                     activeforeground=self.colors['bg'],
                     highlightbackground=self.colors['green'],
                     highlightthickness=2,
                     width=15,
                     command=on_yes_click).pack(side='left', padx=10)
            
            tk.Button(button_frame,
                     text="NO",
                     font=('Courier New', 12, 'bold'),
                     bg=self.colors['bg'],
                     fg=self.colors['amber'],
                     activebackground=self.colors['amber'],
                     activeforeground=self.colors['bg'],
                     highlightbackground=self.colors['border'],
                     highlightthickness=2,
                     width=15,
                     command=on_no_click).pack(side='left', padx=10)
        else:
            tk.Button(button_frame,
                     text="Ok",
                     font=('Courier New', 12, 'bold'),
                     bg=self.colors['bg'],
                     fg=color,
                     activebackground=color,
                     activeforeground=self.colors['bg'],
                     highlightbackground=color,
                     highlightthickness=2,
                     width=20,
                     command=dialog.destroy).pack()
        
        # Center dialog
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (dialog.winfo_width() // 2)
        y = (dialog.winfo_screenheight() // 2) - (dialog.winfo_height() // 2)
        dialog.geometry(f"+{x}+{y}")
        
        # If wait=True, block until the dialog is closed (needed for first-time setup)
        if wait:
            self.root.wait_window(dialog)
    
    def show_ffmpeg_install_dialog(self):
        """Show Jurassic Park themed FFmpeg installation dialog"""
        message = ("⚠️ Optional Component Missing:\n\n"
                  "• FFmpeg Audio Converter (ffmpeg)\n\n"
                  "MP4 and WEBM downloads work without FFmpeg.\n"
                  "MP3 conversion requires FFmpeg.\n\n"
                  "Would you like to install FFmpeg now?")
        
        self.show_themed_dialog(
            "FFmpeg Not Found",
            message,
            dialog_type="warning",
            yes_no=True,
            yes_callback=self.install_ffmpeg
        )
    
    def install_ffmpeg(self):
        """Install FFmpeg using winget"""
        self.log_console("> ")
        self.log_console("> ====================================")
        self.log_console("> FFMPEG INSTALLATION INITIATED")
        self.log_console("> ====================================")
        self.log_console("> ")
        self.log_console("> Attempting to install FFmpeg via winget...")
        self.log_console("> This may take a few moments...")
        self.log_console("> ")
        
        # Disable buttons during installation
        self.btn_check_deps.config(state='disabled')
        self.btn_initiate.config(state='disabled')
        
        # Run installation in thread
        thread = threading.Thread(target=self._install_ffmpeg_thread)
        thread.daemon = True
        thread.start()
    
    def _install_ffmpeg_thread(self):
        """Thread to install FFmpeg"""
        try:
            self.log_console("> Running: winget install Gyan.FFmpeg")
            self.log_console("> ")
            
            # Run winget install with the correct package ID
            result = subprocess.run(
                ['winget', 'install', 'Gyan.FFmpeg', '--accept-package-agreements', '--accept-source-agreements'],
                capture_output=True,
                text=True,
                timeout=300  # 5 minute timeout
            )
            
            # Log output for debugging
            if result.stdout:
                for line in result.stdout.split('\n')[:10]:  # First 10 lines
                    if line.strip():
                        self.log_console(f"> {line.strip()}")
            
            # Check if installation was successful
            success = (result.returncode == 0 or 
                      'successfully installed' in result.stdout.lower() or
                      'already installed' in result.stdout.lower())
            
            if success:
                self.log_console("> ")
                self.log_console("> ====================================")
                self.log_console("> FFMPEG INSTALLED SUCCESSFULLY")
                self.log_console("> ====================================")
                self.log_console("> FFmpeg is now available")
                self.log_console("> MP3 conversion enabled")
                self.log_console("> ")
                self.log_console("> NOTE: You may need to restart the application")
                self.log_console(">       for PATH changes to take effect")
                self.log_console("> ")
                
                self.show_themed_dialog(
                    "Installation Complete",
                    "✓ FFmpeg installed successfully!\n\n"
                    "IMPORTANT: Please restart this application\n"
                    "for changes to take effect.\n\n"
                    "After restart, MP3 downloads will be available!",
                    dialog_type="info"
                )
            else:
                self.log_console("> ")
                self.log_console("> ====================================")
                self.log_console("> INSTALLATION FAILED")
                self.log_console("> ====================================")
                self.log_console(f"> Return code: {result.returncode}")
                if result.stderr:
                    self.log_console(f"> Error: {result.stderr[:300]}")
                self.log_console("> ")
                self.log_console("> Alternative installation methods:")
                self.log_console(">   1. Download from: https://ffmpeg.org")
                self.log_console(">   2. Install via chocolatey: choco install ffmpeg")
                self.log_console(">   3. Try: winget search ffmpeg (to see available packages)")
                self.log_console("> ")
                
                self.show_themed_dialog(
                    "Installation Failed",
                    f"✗ Failed to install FFmpeg automatically.\n\n"
                    f"Manual installation options:\n"
                    f"• Download from: https://ffmpeg.org\n"
                    f"• Use chocolatey: choco install ffmpeg\n"
                    f"• Use scoop: scoop install ffmpeg\n\n"
                    f"MP4 and WEBM downloads still work without FFmpeg.",
                    dialog_type="error"
                )
            
        except subprocess.TimeoutExpired:
            self.log_console("> ERROR: Installation timed out (took > 5 minutes)")
            self.log_console("> Try manual installation from: https://ffmpeg.org")
            self.show_themed_dialog(
                "Installation Timeout",
                f"✗ Installation took too long and was cancelled.\n\n"
                f"Please install manually from:\nhttps://ffmpeg.org",
                dialog_type="error"
            )
        except FileNotFoundError:
            self.log_console("> ERROR: winget not found")
            self.log_console("> winget requires Windows 10 (1809+) or Windows 11")
            self.log_console("> Try manual installation from: https://ffmpeg.org")
            self.show_themed_dialog(
                "winget Not Available",
                f"✗ winget package manager not found.\n\n"
                f"winget requires Windows 10 (1809+) or Windows 11.\n\n"
                f"Please install FFmpeg manually from:\nhttps://ffmpeg.org",
                dialog_type="error"
            )
        except Exception as e:
            self.log_console(f"> ERROR: Installation failed - {str(e)}")
            self.log_console("> Try manual installation from: https://ffmpeg.org")
            self.show_themed_dialog(
                "Installation Error",
                f"✗ Failed to install FFmpeg:\n\n{str(e)}\n\n"
                f"Please install manually from:\nhttps://ffmpeg.org",
                dialog_type="error"
            )
        
        finally:
            # Re-enable buttons
            self.btn_check_deps.config(state='normal')
            self.btn_initiate.config(state='normal')
    
    def install_dependencies(self):
        """Install missing Python dependencies"""
        self.log_console("> ")
        self.log_console("> ====================================")
        self.log_console("> DEPENDENCY INSTALLATION INITIATED")
        self.log_console("> ====================================")
        self.log_console("> ")
        
        # Disable buttons during installation
        self.btn_check_deps.config(state='disabled')
        self.btn_initiate.config(state='disabled')
        
        # Separate Python packages from FFmpeg
        python_packages = [(m, p, d) for m, p, d in self.missing_dependencies if m != 'ffmpeg']
        has_ffmpeg = any(m == 'ffmpeg' for m, p, d in self.missing_dependencies)
        
        if python_packages:
            # Run installation in thread for Python packages
            thread = threading.Thread(target=self._install_deps_thread, args=(python_packages,))
            thread.daemon = True
            thread.start()
        elif has_ffmpeg:
            # Only FFmpeg to install
            self.install_ffmpeg()
    
    def _install_deps_thread(self, packages_list):
        """Thread to install Python dependencies"""
        try:
            packages_to_install = [pkg for _, pkg, _ in packages_list]
            
            for package in packages_to_install:
                self.log_console(f"> Installing {package}...")
                
                # Run pip install
                result = subprocess.run(
                    [sys.executable, '-m', 'pip', 'install', package],
                    capture_output=True,
                    text=True
                )
                
                if result.returncode == 0:
                    self.log_console(f">   {package} .............. INSTALLED")
                else:
                    self.log_console(f">   {package} .............. FAILED")
                    self.log_console(f">   Error: {result.stderr[:100]}")
            
            self.log_console("> ")
            self.log_console("> ====================================")
            self.log_console("> INSTALLATION COMPLETE")
            self.log_console("> ====================================")
            self.log_console("> Please restart the application")
            self.log_console("> ")
            
            self.show_themed_dialog(
                "Installation Complete",
                "✓ Dependencies installed successfully!\n\n"
                "Please restart the application to use the new modules.",
                dialog_type="info"
            )
            
        except Exception as e:
            self.log_console(f"> ERROR: Installation failed - {str(e)}")
            self.show_themed_dialog(
                "Installation Error",
                f"✗ Failed to install dependencies:\n\n{str(e)}",
                dialog_type="error"
            )
        
        finally:
            # Re-enable buttons
            self.btn_check_deps.config(state='normal')
            self.btn_initiate.config(state='normal')


def main():
    """Launch the Jurassic Park themed downloader"""
    root = tk.Tk()
    app = JurassicParkDownloader(root)
    root.mainloop()


if __name__ == "__main__":
    main()

