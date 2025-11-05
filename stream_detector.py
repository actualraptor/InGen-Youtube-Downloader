"""
Stream Detector for BLOB/HLS URLs
Uses Playwright to automatically detect .m3u8 and other stream URLs
"""

import re
from typing import Optional, List, Dict

class StreamDetector:
    """
    Detects real video stream URLs from pages that use blob: URLs
    This is useful for sites like SVT Play that use HLS/DASH streaming
    """
    
    def __init__(self):
        # We'll keep track of whether playwright is available
        self.playwright_available = False
        self.browser = None
        self.context = None
        
        try:
            # Try to import playwright
            from playwright.sync_api import sync_playwright
            self.sync_playwright = sync_playwright
            self.playwright_available = True
        except ImportError:
            # Playwright not installed yet
            self.playwright_available = False
    
    def detect_stream_url(self, page_url: str, timeout: int = 30) -> Optional[Dict[str, any]]:
        """
        Opens a webpage and captures network requests to find the real video stream URL
        
        Args:
            page_url: The URL of the page with the video
            timeout: How long to wait for the stream to appear (seconds)
            
        Returns:
            Dictionary with stream info:
            {
                'url': 'https://...',  # The real stream URL
                'type': 'm3u8' or 'mpd' or 'mp4',
                'all_streams': [...],  # All detected streams
            }
            or None if nothing found
        """
        
        if not self.playwright_available:
            return {
                'error': 'Playwright not installed',
                'url': None,
                'type': None,
                'all_streams': []
            }
        
        detected_streams = []
        best_stream = None
        
        try:
            # Start the browser automation
            with self.sync_playwright() as p:
                # Launch browser in headless mode (invisible)
                browser = p.chromium.launch(headless=True)
                
                # Create a new page
                page = browser.new_page()
                
                # Set up request interceptor to catch video streams
                def handle_request(request):
                    url = request.url
                    
                    # Look for common video stream patterns
                    # .m3u8 = HLS streams (Apple standard)
                    # .mpd = DASH streams (MPEG-DASH)
                    # .ts = Transport Stream segments
                    # .mp4 = Direct MP4 files
                    
                    if any(ext in url.lower() for ext in ['.m3u8', '.mpd', '.ts', '.mp4', 'master', 'playlist']):
                        # Filter out small files and subtitles
                        if 'subtitle' not in url.lower() and 'caption' not in url.lower():
                            stream_type = 'unknown'
                            
                            if '.m3u8' in url or 'master' in url or 'playlist' in url:
                                stream_type = 'm3u8'
                            elif '.mpd' in url:
                                stream_type = 'mpd'
                            elif '.mp4' in url:
                                stream_type = 'mp4'
                            elif '.ts' in url:
                                stream_type = 'ts'
                            
                            detected_streams.append({
                                'url': url,
                                'type': stream_type
                            })
                
                # Listen to all network requests
                page.on("request", handle_request)
                
                # Navigate to the page and wait for it to load
                page.goto(page_url, wait_until="networkidle", timeout=timeout * 1000)
                
                # Wait a bit more to catch lazy-loaded streams
                page.wait_for_timeout(3000)
                
                # Close the browser
                browser.close()
                
                # Find the best stream (prefer .m3u8 master playlists)
                if detected_streams:
                    # Priority: m3u8 > mpd > mp4 > ts
                    for stream in detected_streams:
                        if 'master' in stream['url'].lower() and stream['type'] == 'm3u8':
                            best_stream = stream
                            break
                    
                    if not best_stream:
                        for stream in detected_streams:
                            if stream['type'] == 'm3u8':
                                best_stream = stream
                                break
                    
                    if not best_stream:
                        for stream in detected_streams:
                            if stream['type'] == 'mpd':
                                best_stream = stream
                                break
                    
                    if not best_stream and detected_streams:
                        best_stream = detected_streams[0]
                
                return {
                    'url': best_stream['url'] if best_stream else None,
                    'type': best_stream['type'] if best_stream else None,
                    'all_streams': detected_streams
                }
                
        except Exception as e:
            return {
                'error': str(e),
                'url': None,
                'type': None,
                'all_streams': detected_streams
            }
    
    def is_available(self) -> bool:
        """Check if stream detection is available (Playwright installed)"""
        return self.playwright_available
    
    def install_playwright_browsers(self) -> bool:
        """
        Install Playwright browser binaries
        This needs to be done once after installing playwright
        """
        try:
            import subprocess
            result = subprocess.run(
                ['playwright', 'install', 'chromium'],
                capture_output=True,
                text=True,
                timeout=300  # 5 minutes max
            )
            return result.returncode == 0
        except Exception as e:
            print(f"Failed to install Playwright browsers: {e}")
            return False


# Helper function for easy use
def detect_stream(url: str, timeout: int = 30) -> Optional[Dict[str, any]]:
    """
    Quick helper function to detect a stream URL from a page
    
    Usage:
        result = detect_stream("https://www.svtplay.se/video/...")
        if result and result['url']:
            print(f"Found stream: {result['url']}")
    """
    detector = StreamDetector()
    return detector.detect_stream_url(url, timeout)


if __name__ == "__main__":
    # Test the stream detector
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python stream_detector.py <page_url>")
        sys.exit(1)
    
    test_url = sys.argv[1]
    print(f"Testing stream detection on: {test_url}")
    print("This may take up to 30 seconds...")
    print()
    
    result = detect_stream(test_url)
    
    if result:
        if result.get('error'):
            print(f"❌ Error: {result['error']}")
        elif result.get('url'):
            print(f"✅ Found stream!")
            print(f"   URL: {result['url']}")
            print(f"   Type: {result['type']}")
            print(f"\n📋 All detected streams ({len(result['all_streams'])}):")
            for i, stream in enumerate(result['all_streams'], 1):
                print(f"   {i}. [{stream['type']}] {stream['url']}")
        else:
            print("❌ No streams detected")
            if result['all_streams']:
                print(f"   But found {len(result['all_streams'])} potential URLs")
    else:
        print("❌ Detection failed")

