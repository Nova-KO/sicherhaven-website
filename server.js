const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = process.env.PORT || 8000;

// Serve static files
app.use(express.static('.'));

// Handle 404 errors - serve custom 404.html
app.use((req, res) => {
    const filePath = path.join(__dirname, '404.html');
    
    // Check if 404.html exists
    if (fs.existsSync(filePath)) {
        res.status(404).sendFile(filePath);
    } else {
        // Fallback 404 response
        res.status(404).send(`
            <!DOCTYPE html>
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
            </html>
        `);
    }
});

app.listen(PORT, () => {
    console.log(`Server running at http://localhost:${PORT}/`);
    console.log('Press Ctrl+C to stop the server');
});
