#!/usr/bin/env python3
"""
Simple test server to verify 404 handling
"""

import http.server
import socketserver
import os

class TestHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Get the path
        path = self.path[1:]  # Remove leading slash
        
        # If no path or empty, serve index.html
        if not path:
            path = 'index.html'
        
        # Check if file exists
        if os.path.isfile(path):
            # File exists, serve it normally
            super().do_GET()
        else:
            # File doesn't exist, serve 404.html
            self.send_response(404)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            
            try:
                with open('404.html', 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.wfile.write(content.encode('utf-8'))
                print(f"✅ Served custom 404.html for path: {self.path}")
            except FileNotFoundError:
                # Fallback
                fallback = b"<h1>404 - Page Not Found</h1><p>File not found</p>"
                self.wfile.write(fallback)
                print(f"❌ 404.html not found, served fallback for path: {self.path}")

if __name__ == "__main__":
    PORT = 3000
    
    # Change to script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), TestHTTPRequestHandler) as httpd:
        print(f"Test server running at http://localhost:{PORT}/")
        print(f"Working directory: {os.getcwd()}")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
