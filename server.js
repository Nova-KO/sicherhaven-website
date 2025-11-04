const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const PORT = 8001;

// Serve static files
app.use(express.static('.'));

// URL rewriting based on vercel.json
const rewrites = [
  { source: '/about', destination: '/about.html' },
  { source: '/our-team', destination: '/our-team.html' },
  { source: '/PORTFOLIO', destination: '/PORTFOLIO.html' },
  { source: '/blogs', destination: '/blogs.html' },
  { source: '/contact-us', destination: '/contact-us.html' },
  { source: '/contact', destination: '/contact.html' },
  { source: '/blogspage', destination: '/blogspage.html' },
  { source: '/BLOG', destination: '/BLOG.html' },
  { source: '/INVESTORS', destination: '/INVESTORS.html' },
  { source: '/our-team-single', destination: '/our-team-single.html' },
  { source: '/investors-single', destination: '/investors-single.html' },
  { source: '/PORTFOLIO SINGLE', destination: '/PORTFOLIO SINGLE.html' },
  { source: '/team-single', destination: '/team-single.html' },
  { source: '/404', destination: '/404.html' },
  // Blog posts
  { source: '/blogs/blog-post-1-eventify-community-events', destination: '/blogs/blog-post-1-eventify-community-events.html' },
  { source: '/blogs/blog-post-2-wealthwise-financial-literacy', destination: '/blogs/blog-post-2-wealthwise-financial-literacy.html' },
  { source: '/blogs/blog-post-3-ai-community-engagement', destination: '/blogs/blog-post-3-ai-community-engagement.html' },
  { source: '/blogs/blog-post-4-mobile-app-development', destination: '/blogs/blog-post-4-mobile-app-development.html' },
  { source: '/blogs/blog-post-5-financial-wellness-trends', destination: '/blogs/blog-post-5-financial-wellness-trends.html' },
  { source: '/blogs/blog-post-6-community-building-digital-age', destination: '/blogs/blog-post-6-community-building-digital-age.html' },
  { source: '/blogs/blog-post-7-startup-development-process', destination: '/blogs/blog-post-7-startup-development-process.html' },
  { source: '/blogs/blog-post-8-user-experience-design', destination: '/blogs/blog-post-8-user-experience-design.html' },
  { source: '/blogs/blog-post-9-financial-ai-technology', destination: '/blogs/blog-post-9-financial-ai-technology.html' },
  { source: '/blogs/blog-post-10-innovation-community-finance', destination: '/blogs/blog-post-10-innovation-community-finance.html' },
  { source: '/blogs/ai-financial-technology-blog', destination: '/blogs/ai-financial-technology-blog.html' },
  { source: '/blogs/blog-post', destination: '/blogs/BLOG POST.html' },
  { source: '/blogs/blogpost-templates', destination: '/blogs/blogpost-templates.html' }
];

// Handle rewrites
rewrites.forEach(rewrite => {
  app.get(rewrite.source, (req, res) => {
    const filePath = path.join(__dirname, rewrite.destination);
    if (fs.existsSync(filePath)) {
      res.sendFile(filePath);
    } else {
      res.status(404).send('File not found');
    }
  });
});

// Handle root path
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Handle 404 - serve custom 404.html
app.use((req, res) => {
  res.status(404).sendFile(path.join(__dirname, '404.html'));
});

app.listen(PORT, () => {
  console.log(`🚀 Server running at http://localhost:${PORT}`);
  console.log(`📝 Clean URLs working! Try:`);
  console.log(`   http://localhost:${PORT}/blogs`);
  console.log(`   http://localhost:${PORT}/about`);
  console.log(`   http://localhost:${PORT}/our-team`);
});
