#!/usr/bin/env python3
"""
Simple HTTP server to view the record collection locally.
This avoids CORS issues when loading JSON files.

Usage:
    python3 serve.py

Then open http://localhost:8000 in your browser.
"""

import http.server
import socketserver
import os
import sys

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers to prevent caching during development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"")
        print(f"🎵 Record Collection Server")
        print(f"{'=' * 50}")
        print(f"")
        print(f"✓ Server running at: http://localhost:{PORT}")
        print(f"✓ Open this URL in your browser to view your collection")
        print(f"")
        print(f"Press Ctrl+C to stop the server")
        print(f"")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n\n✓ Server stopped")
            sys.exit(0)

if __name__ == "__main__":
    main()
