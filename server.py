#!/usr/bin/env python3
"""
Custom HTTP server with 404 error handling for Sicherhaven Template
"""
import http.server
import socketserver
import os
import urllib.parse

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the URL
        parsed_path = urllib.parse.urlparse(self.path)
        path = parsed_path.path
        
        # Remove leading slash
        if path.startswith('/'):
            path = path[1:]
        
        # If no path specified, serve index.html
        if not path or path == '':
            path = 'index.html'
        
        # Check if file exists
        if os.path.isfile(path):
            # File exists, serve it normally using the parent class method
            super().do_GET()
        else:
            # File doesn't exist, serve 404.html
            self.send_error_404()
    
    def send_error_404(self):
        """Send custom 404 error page"""
        self.send_response(404)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        
        try:
            with open('404.html', 'r', encoding='utf-8') as f:
                content = f.read()
                self.wfile.write(content.encode('utf-8'))
        except FileNotFoundError:
            # Fallback 404 page if 404.html doesn't exist
            fallback_html = """<!DOCTYPE html>
<html>
<head>
    <title>404 - Page Not Found</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; }
        h1 { color: #e94560; }
        a { color: #0f3460; text-decoration: none; }
        a:hover { text-decoration: underline; }
    </style>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The requested page could not be found.</p>
    <a href="/">Go to Homepage</a>
</body>
</html>"""
            self.wfile.write(fallback_html.encode('utf-8'))

def run_server(port=8000):
    """Run the custom HTTP server"""
    # Change to script directory to ensure 404.html can be found
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    handler = CustomHTTPRequestHandler
    
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Server running at http://localhost:{port}/")
        print(f"Serving files from: {script_dir}")
        print("Press Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")

if __name__ == "__main__":
    import sys
    
    # Get port from command line argument or use default
    port = 8000
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print("Invalid port number. Using default port 8000.")
    
    run_server(port)
