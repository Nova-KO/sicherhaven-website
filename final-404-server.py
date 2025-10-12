#!/usr/bin/env python3
"""
Final working server that serves custom 404 pages
"""

import http.server
import socketserver
import os
import urllib.parse

class Final404Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests"""
        # Parse the path
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        
        # Remove leading slash
        if path.startswith('/'):
            path = path[1:]
        
        # If no path, serve index.html
        if not path:
            path = 'index.html'
        
        # Check if file exists
        if os.path.isfile(path):
            # File exists, serve it
            try:
                with open(path, 'rb') as f:
                    content = f.read()
                
                # Determine content type
                if path.endswith('.html'):
                    content_type = 'text/html; charset=utf-8'
                elif path.endswith('.css'):
                    content_type = 'text/css'
                elif path.endswith('.js'):
                    content_type = 'application/javascript'
                elif path.endswith('.png'):
                    content_type = 'image/png'
                elif path.endswith('.jpg') or path.endswith('.jpeg'):
                    content_type = 'image/jpeg'
                elif path.endswith('.svg'):
                    content_type = 'image/svg+xml'
                else:
                    content_type = 'text/plain'
                
                self.send_response(200)
                self.send_header('Content-Type', content_type)
                self.end_headers()
                self.wfile.write(content)
                print(f"✅ Served file: {path}")
                
            except Exception as e:
                self.send_404()
                print(f"❌ Error serving {path}: {e}")
        else:
            # File doesn't exist, serve 404
            self.send_404()
            print(f"404: File not found: {path}")
    
    def send_404(self):
        """Send custom 404 page"""
        try:
            with open('404.html', 'r', encoding='utf-8') as f:
                content = f.read()
            
            self.send_response(404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(content.encode('utf-8'))
            print(f"✅ Served custom 404.html")
            
        except FileNotFoundError:
            # Fallback if 404.html doesn't exist
            fallback = """<!DOCTYPE html>
<html>
<head>
    <title>404 - Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The requested page could not be found.</p>
    <a href="/">Go to Homepage</a>
</body>
</html>"""
            
            self.send_response(404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(fallback.encode('utf-8'))
            print(f"❌ 404.html not found, served fallback")
            
        except Exception as e:
            # Another fallback
            self.send_response(404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"<h1>404 - Page Not Found</h1>")
            print(f"❌ Error serving 404: {e}")

if __name__ == "__main__":
    PORT = 5000
    
    # Change to script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), Final404Handler) as httpd:
        print(f"Final 404 server running at http://localhost:{PORT}/")
        print(f"Working directory: {os.getcwd()}")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
