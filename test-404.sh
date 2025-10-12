#!/bin/bash
echo "Testing 404 page handling..."
echo "Starting server in background..."
python3 server.py 8000 &
SERVER_PID=$!
sleep 2

echo "Testing home page..."
curl -s http://localhost:8000/ > /dev/null
if [ $? -eq 0 ]; then
    echo "✓ Home page works"
else
    echo "✗ Home page failed"
fi

echo "Testing 404 page..."
response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/nonexistent)
if [ "$response" = "404" ]; then
    echo "✓ 404 page works correctly"
else
    echo "✗ 404 page returned: $response"
fi

echo "Stopping test server..."
kill $SERVER_PID
