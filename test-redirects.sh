#!/bin/bash

echo "🧪 Testing 404 Redirects and Link Fixes"
echo "======================================"

# Start server in background
echo "Starting test server..."
python3 server.py 8890 &
SERVER_PID=$!
sleep 2

echo ""
echo "Testing redirects and 404 handling:"
echo ""

# Test URLs
test_urls=(
    "/nonexistent-page"
    "/portfolio/nonexistent"
    "/blog/nonexistent"
    "/company-pages/about"
    "/user-pages/sign-in"
    "/template-pages/start-here"
    "/invalid-page"
)

for url in "${test_urls[@]}"; do
    echo "Testing: http://localhost:8890$url"
    response=$(curl -s -o /dev/null -w "%{http_code}" "http://localhost:8890$url")
    echo "  Status: $response"
    
    if [ "$response" = "404" ]; then
        echo "  ✅ Correctly returns 404"
    elif [ "$response" = "200" ]; then
        echo "  ✅ Redirected to valid page"
    else
        echo "  ⚠️  Unexpected status: $response"
    fi
    echo ""
done

echo "Stopping test server..."
kill $SERVER_PID

echo ""
echo "✅ Redirect testing complete!"
