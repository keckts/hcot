# Password Reset - Quick Start Guide

## 🎯 What Was Implemented

A complete password reset system using Django's built-in class-based views with custom styling.

## 📋 Quick Test (Development)

1. **Start the server**:
   ```bash
   python manage.py runserver
   ```

2. **Go to login page**: `http://localhost:8000/auth/login/`

3. **Click "Forgot password?"**

4. **Enter any email address** (doesn't need to be real)

5. **Check the terminal/console** - the reset email will be printed there

6. **Copy the reset link** from the console and open it in your browser

7. **Set a new password**

8. **Done!** You can now log in with the new password

## 🔑 Environment Variables for .env

Copy these to your `.env` file:

### Development (Current Setup)
```env
DEBUG=True
DEFAULT_FROM_EMAIL=noreply@localhost
```

### Production (When You Deploy)
```env
DEBUG=False

# Gmail Example
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password-here
DEFAULT_FROM_EMAIL=noreply@yourdomain.com
SERVER_EMAIL=noreply@yourdomain.com
```

## 📧 Email Providers Quick Reference

### Gmail
```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-16-char-app-password
```
**Setup**: Enable 2FA → Generate App Password at https://myaccount.google.com/apppasswords

### SendGrid
```env
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your-sendgrid-api-key
```

### Mailgun
```env
EMAIL_HOST=smtp.mailgun.org
EMAIL_PORT=587
EMAIL_HOST_USER=postmaster@your-domain.mailgun.org
EMAIL_HOST_PASSWORD=your-mailgun-password
```

### AWS SES
```env
EMAIL_HOST=email-smtp.us-east-1.amazonaws.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-aws-access-key-id
EMAIL_HOST_PASSWORD=your-aws-secret-access-key
```

## 📁 Files Created/Modified

### New Files
- `users/templates/users/password_reset_form.html` - Enter email page
- `users/templates/users/password_reset_done.html` - Check email page
- `users/templates/users/password_reset_confirm.html` - Set new password page
- `users/templates/users/password_reset_complete.html` - Success page
- `users/templates/users/password_reset_email.html` - Email template (HTML)
- `users/templates/users/password_reset_subject.txt` - Email subject

### Modified Files
- `users/views.py` - Added `CustomPasswordResetView` and `CustomPasswordResetConfirmView`
- `users/urls.py` - Added 4 password reset URLs
- `users/templates/users/login.html` - Added "Forgot password?" link
- `hcot/settings.py` - Configured email settings
- `.env.example` - Added email configuration variables

### Documentation
- `PASSWORD_RESET_SETUP.md` - Complete documentation
- `PASSWORD_RESET_QUICKSTART.md` - This file

## 🔗 URLs Available

| URL | Purpose |
|-----|---------|
| `/auth/password-reset/` | Request password reset |
| `/auth/password-reset/done/` | Email sent confirmation |
| `/auth/password-reset-confirm/<token>/` | Set new password |
| `/auth/password-reset-complete/` | Success message |

## ✅ Features

- ✅ Beautiful, responsive UI matching your site design
- ✅ Professional HTML email template
- ✅ Toast notifications for success/error messages
- ✅ Secure 24-hour expiring tokens
- ✅ Password validation (minimum 8 chars, not all numeric)
- ✅ Console backend for development
- ✅ SMTP backend for production
- ✅ Works with all major email providers

## 🎨 UI Preview

All pages use:
- Tailwind CSS
- Blue gradient buttons
- Consistent card layout
- Mobile-responsive design
- Toast notifications
- Clean, modern aesthetic

## 🔒 Security

- Tokens expire after 24 hours
- One-time use tokens
- No information leakage (same message whether email exists or not)
- Built on Django's secure auth system
- HTTPS recommended for production

## 📚 Need More Info?

See `PASSWORD_RESET_SETUP.md` for:
- Detailed configuration guide
- Troubleshooting tips
- Customization options
- Security best practices
- Production deployment guide

## 🚀 Next Steps

1. **Test it now** in development (see Quick Test above)
2. **Before production**:
   - Set up email provider (Gmail, SendGrid, etc.)
   - Add credentials to `.env`
   - Set `DEBUG=False`
   - Test with real emails
   - Enable HTTPS

That's it! The password reset system is ready to use. 🎉
