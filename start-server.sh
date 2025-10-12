#!/bin/bash

# Sicherhaven Template Server Startup Script
# This script helps you start the server with proper 404 error handling

echo "🚀 Starting Sicherhaven Template Server..."
echo "=========================================="

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    echo "✅ Python 3 found"
    echo "🌐 Starting server with custom 404 handling..."
    echo "📍 Server will be available at: http://localhost:8000"
    echo "🔗 Try visiting: http://localhost:8000/nonexistent-page to test 404 handling"
    echo ""
    echo "Press Ctrl+C to stop the server"
    echo "=========================================="
    
    # Start the custom Python server
    python3 server.py 8000
elif command -v python &> /dev/null; then
    echo "✅ Python found"
    echo "🌐 Starting server with custom 404 handling..."
    echo "📍 Server will be available at: http://localhost:8000"
    echo "🔗 Try visiting: http://localhost:8000/nonexistent-page to test 404 handling"
    echo ""
    echo "Press Ctrl+C to stop the server"
    echo "=========================================="
    
    # Start the custom Python server
    python server.py 8000
else
    echo "❌ Python not found. Please install Python 3 to run this server."
    echo "Alternatively, you can use:"
    echo "  - Node.js: npm install && npm start"
    echo "  - Standard Python server: python -m http.server 8000 (without 404 handling)"
    exit 1
fi
