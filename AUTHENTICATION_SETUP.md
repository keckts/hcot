# Authentication System Setup Guide

This Django project includes a complete authentication system with Google OAuth support using django-allauth.

## Features

✅ **Email/Password Authentication** - Traditional signup and login
✅ **Google OAuth** - One-click Google sign-in
✅ **Beautiful UI** - Custom-designed login/signup pages with Tailwind CSS
✅ **User Dashboard** - Personalized dashboard for authenticated users
✅ **Auto-redirect** - Authenticated users automatically redirected to dashboard
✅ **Django Cotton Components** - Reusable UI components throughout

## Project Structure

```
hcot/
├── users/                          # Authentication app
│   ├── templates/users/
│   │   ├── login.html             # Login page
│   │   ├── signup.html            # Signup page
│   │   └── dashboard.html         # User dashboard
│   ├── views.py                   # Authentication views
│   └── urls.py                    # Auth URL patterns
├── core/                          # Main app
│   ├── templates/core/
│   │   └── index.html            # Homepage (non-authenticated users)
│   └── views.py                  # Core views with auth redirects
├── templates/cotton/             # Reusable components
│   ├── card.html
│   ├── alert.html
│   ├── badge.html
│   ├── modal.html
│   ├── navbar.html
│   ├── input.html
│   ├── accordion.html
│   ├── gradient_button.html
│   └── loading_button.html
├── .env                          # Environment variables (create this)
├── .env.example                  # Template for .env
└── hcot/settings.py              # Django settings with allauth config
```

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Dependencies include:
- `django-allauth` - Authentication framework
- `python-decouple` - Environment variable management
- `PyJWT` - JWT token handling
- `cryptography` - Cryptographic signing

### 2. Environment Configuration

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` and add your configuration:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Google OAuth Settings
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

### 3. Google OAuth Setup

To enable Google sign-in, you need to create OAuth credentials:

#### Step 1: Create Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the **Google+ API**

#### Step 2: Create OAuth 2.0 Credentials

1. Navigate to **APIs & Services** > **Credentials**
2. Click **Create Credentials** > **OAuth client ID**
3. Choose **Web application**
4. Add authorized redirect URIs:
   ```
   http://localhost:8000/accounts/google/login/callback/
   http://127.0.0.1:8000/accounts/google/login/callback/
   ```
5. Save and copy your **Client ID** and **Client Secret**

#### Step 3: Add Credentials to .env

Paste your credentials into `.env`:

```env
GOOGLE_CLIENT_ID=your-actual-client-id-here.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-actual-client-secret-here
```

### 4. Database Setup

Run migrations to create necessary tables:

```bash
python manage.py migrate
```

### 5. Create Superuser (Optional)

Create an admin account to access Django admin:

```bash
python manage.py createsuperuser
```

### 6. Configure Site Domain

The authentication system requires a Site object:

```bash
python manage.py shell
```

Then in the shell:

```python
from django.contrib.sites.models import Site
site = Site.objects.get(id=1)
site.domain = 'localhost:8000'
site.name = 'HCOT'
site.save()
```

Or through Django admin at `http://localhost:8000/admin/sites/site/`

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Start Tailwind CSS Watcher

In a separate terminal:

```bash
cd theme/static_src
npm run dev
```

## URL Structure

| URL | Purpose | Access |
|-----|---------|--------|
| `/` | Homepage | Public (redirects to /dashboard/ if authenticated) |
| `/auth/login/` | Login page | Public |
| `/auth/signup/` | Signup page | Public |
| `/auth/logout/` | Logout | Authenticated users |
| `/dashboard/` | User dashboard | Authenticated users only |
| `/accounts/google/login/` | Google OAuth | Public |
| `/admin/` | Django admin | Superusers only |

## Authentication Flow

### New User Signup

1. **Visit `/auth/signup/`**
2. **Choose method:**
   - **Google:** Click "Sign up with Google" → Instant account creation
   - **Email:** Fill form → Create account → Redirect to dashboard
3. **Redirected to `/dashboard/`**

### Returning User Login

1. **Visit `/auth/login/`** (or visit `/` when not authenticated)
2. **Choose method:**
   - **Google:** Click "Continue with Google"
   - **Email:** Enter credentials
3. **Redirected to `/dashboard/`**

### Logout

1. **Click "Sign Out" in dashboard navbar**
2. **Redirected to `/` (homepage)**

## Settings Configuration

Key authentication settings in `hcot/settings.py`:

```python
# Authentication Backends
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Allauth Settings
ACCOUNT_LOGIN_METHODS = {"email"}
ACCOUNT_SIGNUP_FIELDS = ["email*", "password1*", "password2*"]
ACCOUNT_EMAIL_VERIFICATION = "optional"

# Redirect URLs
LOGIN_URL = "/auth/login/"
LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/"

# Google OAuth
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": ["profile", "email"],
        "AUTH_PARAMS": {"access_type": "online"},
        "APP": {
            "client_id": config("GOOGLE_CLIENT_ID", default=""),
            "secret": config("GOOGLE_CLIENT_SECRET", default=""),
        },
    }
}
```

## Views Logic

### Core Views (`core/views.py`)

```python
def index(request):
    """Homepage - redirects authenticated users to dashboard."""
    if request.user.is_authenticated:
        return redirect("/dashboard/")
    return render(request, "core/index.html")
```

### Auth Views (`users/views.py`)

```python
@login_required(login_url="/auth/login/")
def dashboard_view(request):
    """Display dashboard for authenticated users."""
    return render(request, "users/dashboard.html")
```

## Customization

### Custom Login/Signup Pages

The project uses custom templates instead of django-allauth's default forms:

- **Login:** `users/templates/users/login.html`
- **Signup:** `users/templates/users/signup.html`

These templates use Django Cotton components for consistent styling.

### Adding More Social Providers

To add GitHub, Facebook, etc.:

1. Install provider: `pip install django-allauth[socialaccount]`
2. Add to `INSTALLED_APPS`:
   ```python
   'allauth.socialaccount.providers.github',
   ```
3. Configure in `SOCIALACCOUNT_PROVIDERS`
4. Add button to login/signup templates

## Security Best Practices

✅ **Environment Variables** - Sensitive data in `.env`, not in code
✅ **HTTPS in Production** - Always use HTTPS for OAuth callbacks
✅ **Secure Cookies** - Set `SESSION_COOKIE_SECURE = True` in production
✅ **CSRF Protection** - Enabled by default in Django
✅ **Password Validation** - Strong password requirements enforced

## Troubleshooting

### Google OAuth Not Working

1. **Check credentials** - Verify `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` in `.env`
2. **Check redirect URI** - Must match exactly in Google Console
3. **Check Site domain** - Update via Django admin or shell
4. **Check migrations** - Run `python manage.py migrate`

### Redirect Loop

1. **Check `LOGIN_URL`** - Should be `/auth/login/`
2. **Check `LOGIN_REDIRECT_URL`** - Should be `/dashboard/`
3. **Clear browser cookies** - Sometimes session data causes issues

### Styling Not Loading

1. **Run Tailwind watcher** - `cd theme/static_src && npm run dev`
2. **Check static files** - `python manage.py collectstatic`
3. **Hard refresh** - Cmd+Shift+R (Mac) or Ctrl+F5 (Windows)

## Production Deployment

Before deploying to production:

1. **Set `DEBUG = False`** in `.env`
2. **Use strong `SECRET_KEY`**
3. **Update `ALLOWED_HOSTS`**
4. **Use HTTPS** for all OAuth callbacks
5. **Set secure cookie flags:**
   ```python
   SESSION_COOKIE_SECURE = True
   CSRF_COOKIE_SECURE = True
   ```
6. **Build Tailwind CSS:** `cd theme/static_src && npm run build`
7. **Collect static files:** `python manage.py collectstatic`

## Testing

Test the authentication flow:

```bash
# Create test user
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Visit http://localhost:8000
# Try login, signup, and Google OAuth
```

## Component Usage in Templates

The authentication pages use Django Cotton components:

```html
<!-- Input field -->
<c-input
    name="email"
    label="Email Address"
    type="email"
    required="true" />

<!-- Alert message -->
<c-alert type="success" title="Welcome!" dismissible="true">
    Login successful!
</c-alert>

<!-- Gradient button -->
<c-gradient_button
    text="Sign In"
    gradient_from="from-purple-500"
    gradient_to="to-blue-500"
    class="w-full" />
```

See `templates/cotton/COMPONENTS.md` for full component documentation.

## Support

For issues or questions:
- Check Django allauth docs: https://django-allauth.readthedocs.io/
- Check Django Cotton docs: https://django-cotton.com/
- Review component docs: `templates/cotton/COMPONENTS.md`

---

**Happy authenticating!** 🔐
