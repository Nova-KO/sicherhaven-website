#!/usr/bin/env python3
"""
Working server that serves custom 404 pages
"""

import http.server
import socketserver
import os

class WorkingHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests"""
        # Get the path
        path = self.path[1:]  # Remove leading slash
        
        # If no path, serve index.html
        if not path:
            path = 'index.html'
        
        # Check if file exists
        if os.path.isfile(path):
            # File exists, serve it normally
            super().do_GET()
        else:
            # File doesn't exist, serve custom 404
            self.send_custom_404()
    
    def send_custom_404(self):
        """Send custom 404 page"""
        try:
            # Read the custom 404.html file
            with open('404.html', 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Send response
            self.send_response(404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
            
            print(f"✅ Served custom 404.html for: {self.path}")
            
        except Exception as e:
            # Fallback if 404.html can't be read
            self.send_response(404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"<h1>404 - Page Not Found</h1><p>Custom 404 page not available</p>")
            print(f"❌ Error serving 404.html: {e}")

if __name__ == "__main__":
    PORT = 3000
    
    # Change to script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print(f"Starting server on port {PORT}...")
    print(f"Working directory: {os.getcwd()}")
    
    # Kill any process using port 3000
    os.system("lsof -ti:3000 | xargs kill -9 2>/dev/null || true")
    
    with socketserver.TCPServer(("", PORT), WorkingHandler) as httpd:
        print(f"Server running at http://localhost:{PORT}/")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
