#!/usr/bin/env python3
"""
Simple server that serves custom 404 pages
"""

import http.server
import socketserver
import os
import urllib.parse

class Custom404Handler(http.server.SimpleHTTPRequestHandler):
    def send_error(self, code, message=None):
        if code == 404:
            # Serve our custom 404 page
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            try:
                with open('404.html', 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.wfile.write(content.encode('utf-8'))
                print(f"✅ Served custom 404.html for: {self.path}")
            except Exception as e:
                # Fallback
                fallback = b"<h1>404 - Page Not Found</h1><p>Custom 404 page not found</p>"
                self.wfile.write(fallback)
                print(f"❌ Error serving 404.html: {e}")
        else:
            # Use default error handling for other codes
            super().send_error(code, message)

if __name__ == "__main__":
    PORT = 3000
    
    # Change to script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), Custom404Handler) as httpd:
        print(f"Custom 404 server running at http://localhost:{PORT}/")
        print(f"Working directory: {os.getcwd()}")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
