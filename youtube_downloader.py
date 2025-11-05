"""
YouTube Video Downloader
Supports multiple formats: MP4, MP3, OGG, WEBM, etc.
"""

import yt_dlp
import os
from pathlib import Path
from typing import Optional


class YouTubeDownloader:
    """Main class for downloading YouTube videos in various formats."""
    
    def __init__(self, download_folder: str = "downloads"):
        """
        Initialize the downloader.
        
        Args:
            download_folder: Path to save downloaded files (default: "downloads")
        """
        self.download_folder = Path(download_folder)
        self.download_folder.mkdir(exist_ok=True)
    
    def download_video(self, url: str, format_type: str = "mp4", quality: str = "best") -> bool:
        """
        Download a video from YouTube.
        
        Args:
            url: YouTube video URL
            format_type: Output format (mp4, mp3, ogg, webm, etc.)
            quality: Quality setting (best, worst, or specific like 720p, 1080p)
        
        Returns:
            True if download successful, False otherwise
        """
        try:
            ydl_opts = self._get_download_options(format_type, quality)
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"\n📥 Downloading from: {url}")
                print(f"📁 Format: {format_type.upper()}")
                print(f"⚙️ Quality: {quality}")
                
                # Get video info first
                info = ydl.extract_info(url, download=False)
                title = info.get('title', 'Unknown')
                print(f"🎬 Title: {title}\n")
                
                # Download
                ydl.download([url])
                
                print(f"\n✅ Download complete! Saved to: {self.download_folder}")
                return True
                
        except Exception as e:
            print(f"\n❌ Error downloading video: {e}")
            return False
    
    def _get_download_options(self, format_type: str, quality: str) -> dict:
        """
        Get yt-dlp options based on format type and quality.
        
        Args:
            format_type: Output format
            quality: Quality setting
        
        Returns:
            Dictionary of yt-dlp options
        """
        base_opts = {
            'outtmpl': str(self.download_folder / '%(title)s.%(ext)s'),
            'progress_hooks': [self._progress_hook],
        }
        
        # Format-specific options
        if format_type.lower() == 'mp3':
            base_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            })
        
        elif format_type.lower() == 'ogg':
            base_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'vorbis',
                    'preferredquality': '192',
                }],
            })
        
        elif format_type.lower() == 'm4a':
            base_opts.update({
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'm4a',
                    'preferredquality': '192',
                }],
            })
        
        elif format_type.lower() in ['mp4', 'webm', 'mkv']:
            # Video formats
            if quality == 'best':
                base_opts['format'] = f'bestvideo[ext={format_type}]+bestaudio[ext=m4a]/best[ext={format_type}]/best'
            elif quality == 'worst':
                base_opts['format'] = f'worstvideo[ext={format_type}]+worstaudio/worst'
            else:
                # Specific resolution (e.g., 720p, 1080p)
                base_opts['format'] = f'bestvideo[height<={quality.replace("p", "")}][ext={format_type}]+bestaudio/best'
            
            base_opts['merge_output_format'] = format_type
        
        else:
            # Default to best quality
            base_opts['format'] = 'best'
        
        return base_opts
    
    def _progress_hook(self, d):
        """Hook to display download progress."""
        if d['status'] == 'downloading':
            if 'downloaded_bytes' in d and 'total_bytes' in d:
                percent = (d['downloaded_bytes'] / d['total_bytes']) * 100
                print(f"\r⏳ Progress: {percent:.1f}%", end='', flush=True)
        elif d['status'] == 'finished':
            print("\r✓ Download finished, now processing...", flush=True)


def main():
    """Main function to run the downloader."""
    print("=" * 60)
    print("🎥 YouTube Downloader".center(60))
    print("=" * 60)
    
    # Initialize downloader
    downloader = YouTubeDownloader(download_folder="downloads")
    
    # Get user input
    print("\n📝 Enter YouTube video URL:")
    url = input("URL: ").strip()
    
    if not url:
        print("❌ No URL provided!")
        return
    
    print("\n📋 Available formats:")
    print("  Video: mp4, webm, mkv")
    print("  Audio: mp3, ogg, m4a")
    
    format_type = input("\n🎯 Choose format (default: mp4): ").strip().lower() or "mp4"
    
    if format_type in ['mp4', 'webm', 'mkv']:
        print("\n📊 Quality options: best, 1080p, 720p, 480p, 360p, worst")
        quality = input("Choose quality (default: best): ").strip().lower() or "best"
    else:
        quality = "best"
    
    # Download
    success = downloader.download_video(url, format_type, quality)
    
    if success:
        print("\n🎉 All done!")
    else:
        print("\n😞 Download failed. Please check the URL and try again.")


if __name__ == "__main__":
    main()



