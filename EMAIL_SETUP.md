# Email Notification Setup Guide

This guide will help you configure email notifications for the contact form.

## Environment Variables

Create a `.env` file in the root directory with the following variables:

### Option 1: Gmail (Recommended for quick setup)

```env
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-app-password-here
EMAIL_FROM=your-email@gmail.com
```

**Important:** For Gmail, you need to use an App Password, not your regular password.

1. Go to [Google Account Settings](https://myaccount.google.com/)
2. Enable 2-Step Verification if not already enabled
3. Go to [App Passwords](https://myaccount.google.com/apppasswords)
4. Generate a new app password for "Mail"
5. Use that password in `EMAIL_PASS`

### Option 2: Custom SMTP Server

```env
SMTP_HOST=smtp.yourdomain.com
SMTP_PORT=587
SMTP_SECURE=false
SMTP_USER=your-smtp-username
SMTP_PASS=your-smtp-password
EMAIL_FROM=noreply@yourdomain.com
```

## Email Recipients

The following email addresses will receive notifications when someone submits the contact form:
- nafih@sicherhaven.com
- anjali@sicherhaven.com
- mohamed.maqsood@sicherhaven.com

These are configured in `server.js` and can be modified if needed.

## Installation

### Local Development

1. Install dependencies:
```bash
npm install
```

2. Create a `.env` file with your email configuration (see above)

3. Start the server:
```bash
npm start
```

### Vercel Deployment

If you're deploying to Vercel, you need to set environment variables in your Vercel project settings:

1. Go to your Vercel project dashboard
2. Navigate to **Settings** → **Environment Variables**
3. Add the following variables:
   - `EMAIL_USER` (for Gmail) or `SMTP_USER` (for custom SMTP)
   - `EMAIL_PASS` (for Gmail) or `SMTP_PASS` (for custom SMTP)
   - `EMAIL_FROM` (sender email address)
   - If using custom SMTP, also add: `SMTP_HOST`, `SMTP_PORT`, `SMTP_SECURE`

4. Redeploy your project after adding the environment variables

The API endpoint `/api/contact` will automatically work as a serverless function on Vercel.

## Testing

1. Fill out the contact form on the contact page
2. Submit the form
3. Check the three email addresses for the notification

## Troubleshooting

- **Emails not sending**: Check that your environment variables are set correctly
- **Gmail authentication errors**: Make sure you're using an App Password, not your regular password
- **SMTP errors**: Verify your SMTP server settings and credentials
