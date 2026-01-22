require('dotenv').config();
const express = require('express');
const path = require('path');
const fs = require('fs');
const nodemailer = require('nodemailer');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const PORT = 8001;

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

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

// Email configuration - using environment variables
const createTransporter = () => {
  // If SMTP credentials are provided, use them
  if (process.env.SMTP_HOST && process.env.SMTP_USER && process.env.SMTP_PASS) {
    return nodemailer.createTransport({
      host: process.env.SMTP_HOST,
      port: parseInt(process.env.SMTP_PORT || '587'),
      secure: process.env.SMTP_SECURE === 'true',
      auth: {
        user: process.env.SMTP_USER,
        pass: process.env.SMTP_PASS
      }
    });
  }

  // Default: Use Gmail with OAuth2 or App Password
  // For Gmail, you'll need to use an App Password or OAuth2
  return nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: process.env.EMAIL_USER || process.env.SMTP_USER,
      pass: process.env.EMAIL_PASS || process.env.SMTP_PASS
    }
  });
};

// Contact form submission endpoint
app.post('/api/contact', async (req, res) => {
  try {
    const { 'First-Name': firstName, 'Last-Name': lastName, Email, 'Phone-Number': phoneNumber, Company, Message } = req.body;

    // Validate required fields
    if (!firstName || !lastName || !Email) {
      return res.status(400).json({
        success: false,
        error: 'Missing required fields'
      });
    }

    // Recipient emails
    const recipientEmails = [
      'nafih@sicherhaven.com',
      'anjali@sicherhaven.com',
      'mohamed.maqsood@sicherhaven.com'
    ];

    // Create email content
    const emailSubject = `New Contact Form Submission from ${firstName} ${lastName}`;
    const emailHtml = `
      <h2>New Contact Form Submission</h2>
      <p><strong>Name:</strong> ${firstName} ${lastName}</p>
      <p><strong>Email:</strong> ${Email}</p>
      <p><strong>Phone:</strong> ${phoneNumber || 'Not provided'}</p>
      <p><strong>Company:</strong> ${Company || 'Not provided'}</p>
      <p><strong>Message:</strong></p>
      <p>${Message || 'No message provided'}</p>
      <hr>
      <p><small>This email was sent from the Sicherhaven contact form.</small></p>
    `;

    const emailText = `
New Contact Form Submission

Name: ${firstName} ${lastName}
Email: ${Email}
Phone: ${phoneNumber || 'Not provided'}
Company: ${Company || 'Not provided'}

Message:
${Message || 'No message provided'}

---
This email was sent from the Sicherhaven contact form.
    `;

    // Create transporter
    const transporter = createTransporter();

    // Send email to all recipients
    const emailPromises = recipientEmails.map(recipient => {
      return transporter.sendMail({
        from: process.env.EMAIL_FROM || process.env.SMTP_USER || 'noreply@sicherhaven.com',
        to: recipient,
        subject: emailSubject,
        text: emailText,
        html: emailHtml
      });
    });

    await Promise.all(emailPromises);

    // Send data to Google Sheets
    try {
      const googleSheetUrl = 'https://script.google.com/macros/s/AKfycbyNJJ9yW6ueaPNT3vR_2dVQlryD82xmJD_7VneHaTxKr26dAae2EQw0FlNf0PAx_RDo/exec';
      await fetch(googleSheetUrl, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(req.body)
      });
    } catch (sheetError) {
      console.error('Google Sheets error:', sheetError);
      // We don't fail the request if the sheet update fails, as the email was sent successfully
    }

    res.json({
      success: true,
      message: 'Form submitted successfully. We will get back to you soon!'
    });

  } catch (error) {
    console.error('Error sending email:', error);
    res.status(500).json({
      success: false,
      error: 'Failed to send email notification. Please try again later.'
    });
  }
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
