const nodemailer = require('nodemailer');

// Email configuration helper
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
  
  // Default: Use Gmail with App Password
  return nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: process.env.EMAIL_USER || process.env.SMTP_USER,
      pass: process.env.EMAIL_PASS || process.env.SMTP_PASS
    }
  });
};

module.exports = async (req, res) => {
  // Enable CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');

  // Handle preflight requests
  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  // Only allow POST requests
  if (req.method !== 'POST') {
    return res.status(405).json({ 
      success: false, 
      error: 'Method not allowed' 
    });
  }

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
        from: process.env.EMAIL_FROM || process.env.SMTP_USER || process.env.EMAIL_USER || 'noreply@sicherhaven.com',
        to: recipient,
        subject: emailSubject,
        text: emailText,
        html: emailHtml
      });
    });

    await Promise.all(emailPromises);

    res.status(200).json({ 
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
};
