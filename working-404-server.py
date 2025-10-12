#!/usr/bin/env python3
"""
Working server that serves custom 404 pages by overriding the correct method
"""

import http.server
import socketserver
import os

class Working404Handler(http.server.SimpleHTTPRequestHandler):
    def send_error(self, code, message=None, explain=None):
        """Override send_error to serve custom 404 page"""
        if code == 404:
            try:
                # Read our custom 404 page
                with open('404.html', 'r', encoding='utf-8') as f:
                    error_content = f.read()
                
                # Send the custom 404 page
                self.send_response(404)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(error_content.encode('utf-8'))
                
                print(f"✅ Served custom 404.html for: {self.path}")
                
            except FileNotFoundError:
                # If 404.html doesn't exist, use default
                super().send_error(code, message, explain)
                print(f"❌ 404.html not found, used default error")
            except Exception as e:
                # If any other error, use default
                super().send_error(code, message, explain)
                print(f"❌ Error serving 404.html: {e}")
        else:
            # For other error codes, use default behavior
            super().send_error(code, message, explain)

if __name__ == "__main__":
    PORT = 3000
    
    # Change to script directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), Working404Handler) as httpd:
        print(f"Working 404 server running at http://localhost:{PORT}/")
        print(f"Working directory: {os.getcwd()}")
        print("Press Ctrl+C to stop")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
