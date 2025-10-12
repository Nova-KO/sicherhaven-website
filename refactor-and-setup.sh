#!/bin/bash

echo "╔════════════════════════════════════════════════════════════╗"
echo "║  Sicherhaven Template - Component Refactoring & Setup     ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Check if Python 3 is installed
echo -e "${BLUE}[1/5]${NC} Checking Python installation..."
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}✗ Python 3 is not installed. Please install Python 3 to continue.${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Python 3 found${NC}"
echo ""

# Install Python dependencies
echo -e "${BLUE}[2/5]${NC} Installing Python dependencies..."
if python3 -c "import bs4" 2>/dev/null; then
    echo -e "${GREEN}✓ beautifulsoup4 already installed${NC}"
else
    echo "Installing beautifulsoup4..."
    pip3 install beautifulsoup4 || python3 -m pip install beautifulsoup4
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ beautifulsoup4 installed${NC}"
    else
        echo -e "${RED}✗ Failed to install beautifulsoup4${NC}"
        exit 1
    fi
fi
echo ""

# Run the refactoring script
echo -e "${BLUE}[3/5]${NC} Running component refactoring script..."
chmod +x refactor-components.py
python3 refactor-components.py
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Refactoring completed successfully${NC}"
else
    echo -e "${RED}✗ Refactoring failed${NC}"
    exit 1
fi
echo ""

# Test if the server can start
echo -e "${BLUE}[4/5]${NC} Verifying server configuration..."
if [ -f "server.py" ]; then
    echo -e "${GREEN}✓ Python server (server.py) found${NC}"
fi
if [ -f "server.js" ]; then
    echo -e "${GREEN}✓ Node.js server (server.js) found${NC}"
fi
echo ""

# Create a test script
echo -e "${BLUE}[5/5]${NC} Creating test script..."
cat > test-404.sh << 'EOF'
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
EOF
chmod +x test-404.sh
echo -e "${GREEN}✓ Test script created (test-404.sh)${NC}"
echo ""

echo "╔════════════════════════════════════════════════════════════╗"
echo "║              Setup Complete! 🎉                            ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo ""
echo "What was done:"
echo "  ✓ Extracted header and footer into components"
echo "  ✓ Created Sicherhaven-specific footer content"
echo "  ✓ Updated all HTML pages with new footer"
echo "  ✓ Fixed server 404 handling"
echo ""
echo "Next steps:"
echo "  1. Start server: ${GREEN}./start-server.sh${NC}"
echo "  2. View site: ${BLUE}http://localhost:8000/${NC}"
echo "  3. Test 404: ${BLUE}http://localhost:8000/test${NC}"
echo "  4. Run tests: ${GREEN}./test-404.sh${NC}"
echo ""
echo "Alternative commands:"
echo "  • Python server: ${YELLOW}python3 server.py${NC}"
echo "  • Node server: ${YELLOW}npm install && npm start${NC}"
echo ""

