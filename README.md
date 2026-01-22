# Sicherhaven Technologies Website

A modern, responsive website for Sicherhaven Technologies built with clean URLs, organized file structure, and Vercel deployment support.

## 🚀 Features

- **Clean URLs**: No .html extensions in URLs (e.g., `/blogs` instead of `/blogs.html`)
- **Organized Structure**: Blog posts in `blogs/` folder, images in `img/` folder
- **Vercel Ready**: Configured for seamless deployment on Vercel
- **Local Development**: Express server with URL rewriting for development
- **Responsive Design**: Mobile-first responsive design
- **SEO Optimized**: Clean URLs and proper meta tags

## 📁 Project Structure

```
/Sicherhaven Template/
├── img/                     # 📁 Images and SVGs
│   ├── logo251.81.png
│   ├── logoblack2.png
│   ├── logov2.png
│   ├── logo.svg
│   ├── logodark.svg
│   ├── logo-optimized.svg
│   └── nobg2.svg
├── blogs/                   # 📁 Blog posts
│   ├── blog-post-1-eventify-community-events.html
│   ├── blog-post-2-wealthwise-financial-literacy.html
│   ├── blog-post-3-ai-community-engagement.html
│   ├── blog-post-4-mobile-app-development.html
│   ├── blog-post-5-financial-wellness-trends.html
│   ├── blog-post-6-community-building-digital-age.html
│   ├── blog-post-7-startup-development-process.html
│   ├── blog-post-8-user-experience-design.html
│   ├── blog-post-9-financial-ai-technology.html
│   ├── blog-post-10-innovation-community-finance.html
│   ├── ai-financial-technology-blog.html
│   ├── BLOG POST.html
│   └── blogpost-templates.html
├── components/              # 📁 Reusable components
│   ├── footer.html
│   ├── header.html
│   ├── header-dark.html
│   └── hero-about.html
├── index.html              # 🏠 Homepage
├── about.html              # ℹ️ About page
├── our-team.html           # 👥 Team page
├── blogs.html              # 📝 Blog listing page
├── blogspage.html          # 📄 Blog page
├── PORTFOLIO.html          # 💼 Portfolio page
├── contact-us.html         # 📞 Contact page
├── INVESTORS.html          # 💰 Investors page
├── vercel.json             # ⚙️ Vercel configuration
├── server.js               # 🖥️ Local development server
├── package.json            # 📦 Node.js dependencies
└── README.md               # 📖 This file
```

## 🛠️ Development

### Prerequisites
- Node.js (v14 or higher)
- npm or yarn

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/Nova-KO/sicherhaven-website.git
   cd sicherhaven-website
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm start
   ```

4. **Open in browser**
   ```
   http://localhost:8001
   ```

### Clean URLs in Development

The local server supports clean URLs just like production:

- `http://localhost:8001/` → Homepage
- `http://localhost:8001/about` → About page
- `http://localhost:8001/our-team` → Team page
- `http://localhost:8001/blogs` → Blog listing
- `http://localhost:8001/blogs/blog-post-1-eventify-community-events` → Blog post

## 🚀 Deployment

### Vercel Deployment

1. **Connect to Vercel**
   - Import your GitHub repository to Vercel
   - Vercel will automatically detect the `vercel.json` configuration

2. **Automatic Clean URLs**
   - The `vercel.json` file handles all URL rewriting
   - No additional configuration needed

3. **Deploy**
   - Push to main branch triggers automatic deployment
   - Clean URLs work immediately after deployment

### Manual Deployment

1. **Build** (if needed)
   ```bash
   # No build step required for static HTML
   ```

2. **Deploy to any static hosting**
   - Upload all files to your hosting provider
   - Ensure `vercel.json` is included for URL rewriting

## 🔧 Configuration

### URL Rewriting

The `vercel.json` file contains all URL rewriting rules:

```json
{
  "rewrites": [
    { "source": "/about", "destination": "/about.html" },
    { "source": "/blogs", "destination": "/blogs.html" },
    { "source": "/blogs/blog-post-1-eventify-community-events", "destination": "/blogs/blog-post-1-eventify-community-events.html" }
  ],
  "redirects": [
    { "source": "/about.html", "destination": "/about", "permanent": true }
  ]
}
```

### Adding New Pages

1. **Create HTML file** (e.g., `new-page.html`)
2. **Add to vercel.json**:
   ```json
   {
     "source": "/new-page",
     "destination": "/new-page.html"
   }
   ```
3. **Update navigation** in HTML files
4. **Commit and push**

### Adding New Blog Posts

1. **Create blog post** in `blogs/` folder
2. **Add to vercel.json**:
   ```json
   {
     "source": "/blogs/new-blog-post",
     "destination": "/blogs/new-blog-post.html"
   }
   ```
3. **Update blog listing** if needed

## 📱 Pages

- **Homepage** (`/`) - Landing page with hero section
- **About** (`/about`) - Company information
- **Team** (`/our-team`) - Team members and profiles
- **Blog** (`/blogs`) - Blog posts and articles
- **Portfolio** (`/PORTFOLIO`) - Project showcase
- **Contact** (`/contact-us`) - Contact information and form
- **Investors** (`/INVESTORS`) - Investor information

## 🎨 Styling

- **CSS Variables**: Custom properties for consistent theming
- **Responsive Design**: Mobile-first approach
- **Modern Layout**: CSS Grid and Flexbox
- **Typography**: Inter Tight font family
- **Colors**: Custom color scheme with dark/light variants

## 📦 Dependencies

- **Express**: Local development server
- **No build tools**: Pure HTML, CSS, and JavaScript
- **Vercel**: Deployment platform

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally with `npm start`
5. Commit and push
6. Create a pull request

## 📄 License

This project is licensed under the MIT License.

## 🔗 Links

- **Live Site**: [Deploy to Vercel](https://vercel.com)
- **Repository**: [GitHub](https://github.com/Nova-KO/sicherhaven-website)
- **Documentation**: This README

---

**Sicherhaven Technologies** - Building innovative solutions for community events and financial wellness through Eventify and WealthWise.
