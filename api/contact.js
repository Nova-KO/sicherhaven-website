const nodemailer = require('nodemailer');

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ message: 'Method not allowed' });
  }

  const { 'First-Name': firstName, 'Last-Name': lastName, Email, 'Phone-Number': phoneNumber, Company, Message } = req.body;

  if (!firstName || !lastName || !Email) {
    return res.status(400).json({ success: false, error: 'Missing required fields' });
  }

  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: 'novakopro@gmail.com',
      pass: 'nnfn urrj bqbv xoys'
    }
  });

  const recipients = [
    'nafih@sicherhaven.com',
    'anjali@sicherhaven.com',
    'mohamed.maqsood@sicherhaven.com'
  ];

  const subject = `New Contact Form Submission from ${firstName} ${lastName}`;
  const htmlContent = `
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

  try {
    await transporter.sendMail({
      from: '"Sicherhaven Website" <novakopro@gmail.com>',
      to: recipients.join(', '),
      subject: subject,
      html: htmlContent
    });

    res.status(200).json({ success: true, message: 'Email sent successfully' });
  } catch (error) {
    console.error('Email error:', error);
    res.status(500).json({ success: false, error: 'Failed to send email' });
  }
}
