# Password Reset System Documentation

A complete, production-ready password reset system using Django's built-in class-based views with custom styling and email templates.

## Features

✅ **Secure Token-Based Reset** - Uses Django's secure token generation
✅ **Beautiful Email Templates** - Professional HTML email design
✅ **Responsive UI** - Mobile-friendly reset pages
✅ **Toast Notifications** - Success/error messages with smooth animations
✅ **Multiple Email Providers** - Supports Gmail, SendGrid, Mailgun, AWS SES, etc.
✅ **Development & Production Ready** - Console backend for dev, SMTP for production
✅ **24-Hour Expiry** - Reset links automatically expire after 24 hours
✅ **User-Friendly Flow** - Clear instructions and error handling

## User Flow

1. **User clicks "Forgot Password?"** on login page
2. **Enters email address** on password reset form
3. **Receives email** with reset link (or sees in console during development)
4. **Clicks link** in email to access password reset page
5. **Sets new password** with validation
6. **Success confirmation** with redirect to login

## File Structure

```
users/
├── views.py                          # Password reset views
├── urls.py                           # URL routing
├── templates/users/
│   ├── login.html                    # Updated with "Forgot Password?" link
│   ├── password_reset_form.html      # Step 1: Enter email
│   ├── password_reset_done.html      # Step 2: Check email message
│   ├── password_reset_confirm.html   # Step 3: Set new password
│   ├── password_reset_complete.html  # Step 4: Success message
│   ├── password_reset_email.html     # HTML email template
│   └── password_reset_subject.txt    # Email subject line

hcot/
└── settings.py                       # Email configuration

.env.example                          # Environment variables template
```

## Configuration

### 1. Environment Variables

All email settings are configured via environment variables in `.env`:

#### Development (Default)
```env
DEBUG=True
DEFAULT_FROM_EMAIL=noreply@localhost
```

In development mode, emails are printed to the console instead of being sent.

#### Production
```env
DEBUG=False

# Gmail Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password-here
DEFAULT_FROM_EMAIL=noreply@yourdomain.com
SERVER_EMAIL=noreply@yourdomain.com
```

### 2. Email Provider Setup

#### Gmail

1. Enable 2-factor authentication on your Google account
2. Go to [App Passwords](https://myaccount.google.com/apppasswords)
3. Generate a new app password for "Mail"
4. Use this password as `EMAIL_HOST_PASSWORD`

```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-16-char-app-password
```

#### SendGrid

```env
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your-sendgrid-api-key
```

#### Mailgun

```env
EMAIL_HOST=smtp.mailgun.org
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=postmaster@your-domain.mailgun.org
EMAIL_HOST_PASSWORD=your-mailgun-password
```

#### AWS SES

```env
EMAIL_HOST=email-smtp.us-east-1.amazonaws.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-aws-access-key-id
EMAIL_HOST_PASSWORD=your-aws-secret-access-key
```

#### Outlook/Hotmail

```env
EMAIL_HOST=smtp-mail.outlook.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@outlook.com
EMAIL_HOST_PASSWORD=your-password
```

## URL Endpoints

The following URLs are available:

| URL | Name | Purpose |
|-----|------|---------|
| `/auth/password-reset/` | `users:password_reset` | Enter email form |
| `/auth/password-reset/done/` | `users:password_reset_done` | Check email message |
| `/auth/password-reset-confirm/<uidb64>/<token>/` | `users:password_reset_confirm` | Set new password |
| `/auth/password-reset-complete/` | `users:password_reset_complete` | Success message |

## Views

### CustomPasswordResetView

Custom implementation of Django's `PasswordResetView` with:
- Custom template
- Success message via Django messages framework
- Email template configuration

**Location**: `users/views.py:184-203`

### CustomPasswordResetConfirmView

Custom implementation of Django's `PasswordResetConfirmView` with:
- Custom template
- Success message via Django messages framework
- Validation and error handling

**Location**: `users/views.py:206-223`

## Templates

### 1. Password Reset Form (`password_reset_form.html`)

**Purpose**: User enters their email address to request a password reset

**Features**:
- Clean, modern design matching your login page
- Email validation
- "Back to login" link
- "Sign up" link for new users

### 2. Password Reset Done (`password_reset_done.html`)

**Purpose**: Confirmation that email has been sent

**Features**:
- Success icon and message
- Step-by-step instructions
- "Back to Login" button
- "Try again" link
- Security note about 24-hour expiry

### 3. Password Reset Confirm (`password_reset_confirm.html`)

**Purpose**: User sets their new password using the token from email

**Features**:
- Password strength requirements display
- Confirm password field
- Error handling for invalid/expired links
- "Request New Link" button for expired tokens

### 4. Password Reset Complete (`password_reset_complete.html`)

**Purpose**: Success confirmation after password is reset

**Features**:
- Success icon and message
- "Continue to Login" button
- Security tip about password management

### 5. Password Reset Email (`password_reset_email.html`)

**Purpose**: HTML email sent to user with reset link

**Features**:
- Professional gradient design
- Prominent "Reset Password" button
- Copy-paste link fallback
- 24-hour expiry notice
- Security warning about ignoring if not requested

## Testing

### Development Testing

1. Start the development server:
```bash
python manage.py runserver
```

2. Navigate to login page: `http://localhost:8000/auth/login/`

3. Click "Forgot password?"

4. Enter an email address (doesn't need to be real in dev mode)

5. Check the **console/terminal** where the server is running - you'll see the email printed there

6. Copy the reset link from the console and paste it into your browser

7. Set a new password

8. Verify you can log in with the new password

### Production Testing

1. Configure email settings in `.env`
2. Set `DEBUG=False`
3. Test with a real email address
4. Check your inbox (and spam folder)
5. Click the link in the email
6. Complete the password reset

## Security Features

### Built-in Django Security

- **Secure Token Generation**: Uses Django's `PasswordResetTokenGenerator`
- **Time-Limited Tokens**: Links expire after 24 hours (configurable)
- **One-Time Use**: Tokens are invalidated after use
- **User Verification**: Only works for existing user accounts
- **Password Validation**: Enforces minimum length and complexity

### Additional Security

- **No Information Leakage**: Same message shown whether email exists or not
- **HTTPS Recommended**: Always use HTTPS in production
- **Email Obfuscation**: Doesn't reveal if an email is registered
- **Rate Limiting**: Consider adding rate limiting to prevent abuse (not implemented yet)

## Customization

### Change Token Expiry Time

In `settings.py`, add:

```python
PASSWORD_RESET_TIMEOUT = 86400  # 24 hours (in seconds)
# Or: 3600 = 1 hour, 43200 = 12 hours
```

### Customize Email Template

Edit `users/templates/users/password_reset_email.html`:

- Change colors by modifying the gradient values
- Update company name/branding
- Add logo or header image
- Modify footer text

### Customize Success Messages

Edit the messages in `users/views.py`:

```python
# Line 199 - Email sent message
messages.success(
    self.request,
    "Your custom message here"
)

# Line 219 - Password reset success message
messages.success(
    self.request,
    "Your custom message here"
)
```

## Troubleshooting

### Emails Not Sending

**Issue**: No emails received in production

**Solutions**:
1. Check email credentials in `.env`
2. Verify `DEBUG=False` in production
3. Check spam/junk folder
4. Verify email provider allows SMTP
5. Check server logs for errors
6. Test SMTP connection:
   ```bash
   python manage.py shell
   from django.core.mail import send_mail
   send_mail('Test', 'Test', 'from@example.com', ['to@example.com'])
   ```

### Invalid/Expired Token

**Issue**: "Invalid reset link" message

**Solutions**:
- Token may have expired (24 hours)
- Token already used
- URL may be malformed
- Request a new reset link

### Gmail App Password Not Working

**Issue**: Gmail authentication fails

**Solutions**:
1. Enable 2FA on Google account
2. Generate new app password
3. Use app password, not regular password
4. Remove spaces from app password
5. Check "Less secure app access" is disabled (use app passwords instead)

### Console Backend Not Showing Emails

**Issue**: Emails not appearing in development console

**Solutions**:
1. Verify `DEBUG=True`
2. Check console output carefully
3. Email appears after form submission
4. Check `EMAIL_BACKEND` setting

## Integration with Existing Features

### Toast Notifications

The password reset system integrates with your existing toast notification system (`<c-notifications />`):

- ✅ Success messages appear as green toasts
- ✅ Error messages appear as red toasts
- ✅ Auto-dismiss after 2 seconds
- ✅ Smooth slide-in animations

### Styling

All templates use:
- Tailwind CSS utility classes
- Gradient buttons matching login/signup
- Consistent color scheme (blue gradients)
- Responsive design (mobile-friendly)
- Same card layout as other auth pages

## Best Practices

### For Development

1. ✅ Use console backend (`DEBUG=True`)
2. ✅ Test with any email address
3. ✅ Copy links from console
4. ✅ Test all error scenarios

### For Production

1. ✅ Use real SMTP service
2. ✅ Set up app passwords (don't use main password)
3. ✅ Configure `DEFAULT_FROM_EMAIL`
4. ✅ Use HTTPS for all pages
5. ✅ Monitor email delivery rates
6. ✅ Set up email logs/alerts
7. ✅ Consider adding rate limiting
8. ✅ Regular security audits

## Future Enhancements

Potential improvements:

- [ ] Add rate limiting to prevent abuse
- [ ] Two-factor authentication integration
- [ ] Password strength meter on reset page
- [ ] Email verification after password change
- [ ] Account activity notifications
- [ ] Custom password validators
- [ ] Passwordless login option
- [ ] Social auth password reset handling

## Support

For issues or questions:
- Check Django documentation: https://docs.djangoproject.com/en/stable/topics/auth/
- Review Django auth source code
- Check email provider documentation

## License

This implementation uses Django's built-in authentication system and is subject to Django's BSD license.
