# Sicherhaven Template

A modern, responsive website template for Sicherhaven - building innovative solutions for community events and financial wellness.

## 🎯 Features

- **Custom 404 Page**: Beautiful, branded 404 error page with auto-redirect
- **Component-Based Architecture**: Modular header and footer components
- **Dual Server Support**: Python and Node.js server options
- **Sicherhaven Branding**: Customized footer with company-specific content
- **Responsive Design**: Mobile-first, modern UI/UX

## 🚀 Quick Start

### Option 1: Using the Start Script (Recommended)

```bash
./start-server.sh
```

Then visit: http://localhost:8000/

### Option 2: Python Server

```bash
python3 server.py
# Or specify a custom port:
python3 server.py 3000
```

### Option 3: Node.js Server

```bash
npm install
npm start
```

## 📁 Project Structure

```
Sicherhaven Template/
├── components/          # Reusable header and footer components
│   └── footer.html     # Sicherhaven-specific footer
├── *.html              # Website pages
├── server.py           # Python HTTP server with 404 handling
├── server.js           # Node.js Express server with 404 handling
├── 404.html            # Custom 404 error page
├── start-server.sh     # Quick start script
├── refactor-components.py  # Component extraction script
└── refactor-and-setup.sh   # Automated setup script
```

## 🛠️ Development

### Refactoring Components

If you need to re-run the component refactoring:

```bash
./refactor-and-setup.sh
```

This script will:
1. Extract header and footer into component files
2. Update all HTML pages with the new footer
3. Fix server 404 handling
4. Create test scripts

### Testing

Test the 404 page handling:

```bash
./test-404.sh
```

Or manually:
1. Start the server
2. Visit http://localhost:8000/nonexistent-page
3. You should see the custom 404 page

## 📄 Pages

- `index.html` - Homepage with product showcase
- `Contact.html` - Contact form
- `BLOG.html` - Blog listing
- `BLOG POST.html` - Individual blog post
- `PORTFOLIO.html` - Portfolio/Products page
- `PORTFOLIO SINGLE.html` - Individual product page
- `INVESTORS.html` - Team/Investors page
- `INVESTORS SINGLE.html` - Individual team member
- `coming soon.html` - Coming soon page
- `404.html` - Custom 404 error page

## 🎨 Customization

### Updating the Footer

The footer content is Sicherhaven-specific and includes:
- Company tagline
- Product links (Eventify, WealthWise)
- Company pages (About, Contact, Blog)
- Social media links (Twitter, LinkedIn, GitHub)
- Copyright notice

To modify the footer:
1. Edit `components/footer.html`
2. Run `python3 refactor-components.py` to apply changes

### Updating the 404 Page

Edit `404.html` to customize:
- Error message
- Product links
- Redirect timeout (default: 10 seconds)
- Styling

## 🔧 Server Configuration

### Python Server (server.py)

Features:
- Custom 404 handling
- Serves static files
- Automatic directory detection
- Configurable port

```python
# Default port: 8000
python3 server.py

# Custom port:
python3 server.py 3000
```

### Node.js Server (server.js)

Features:
- Express-based
- Custom 404 middleware
- Static file serving
- Environment variable support

```bash
# Default port: 8000
npm start

# Custom port:
PORT=3000 npm start
```

## 📦 Dependencies

### Python
- Python 3.6+
- beautifulsoup4 (for refactoring script)

### Node.js
- Node.js 14+
- express ^4.18.2

## 🔍 Troubleshooting

### Port Already in Use

If you see "Address already in use":

```bash
# Kill process on port 8000
lsof -ti:8000 | xargs kill -9

# Or use a different port
python3 server.py 3001
```

### 404 Page Not Showing

1. Ensure `404.html` exists in the root directory
2. Verify server is running from the correct directory
3. Check server logs for errors
4. Test with: `curl -I http://localhost:8000/nonexistent`

### Footer Not Updating

1. Run the refactoring script: `./refactor-and-setup.sh`
2. Clear browser cache
3. Check `components/footer.html` exists
4. Verify HTML files have `<div class="footer-container">`

## 📚 Scripts Reference

| Script | Description |
|--------|-------------|
| `start-server.sh` | Start the server (auto-detects Python/Node) |
| `refactor-and-setup.sh` | Full setup and refactoring |
| `refactor-components.py` | Extract and inject components |
| `test-404.sh` | Test 404 page handling |

## 🎯 Products

### Eventify
A community-powered application to help people discover local events and provide more exposure for event hosts and organizers.

### WealthWise
An AI-powered wealth monitoring application that helps users understand their finances, credit history, utilizations, and identify redundant fees for better financial literacy.

## 📞 Support

For issues or questions:
- Check the troubleshooting section
- Review server logs
- Verify all files are in place

## 📄 License

Copyright © 2024 Sicherhaven | Building the future of community events and financial wellness

---

Made with ❤️ by Sicherhaven

