# Authentication Testing Guide

## ✅ Everything is Now Working!

Your authentication system has been converted to clean **Function-Based Views (FBVs)** and is fully functional.

## 🧪 Test Credentials

A test user has been created for you:
```
Username: testuser
Password: testpass123
```

## 📋 How to Test

### 1. Start the Development Server

```bash
# Terminal 1: Django server
python manage.py runserver

# Terminal 2: Tailwind CSS watcher
cd theme/static_src
npm run dev
```

### 2. Test Login Flow

1. **Visit:** `http://localhost:8000/auth/login/`
2. **Enter:**
   - Username: `testuser`
   - Password: `testpass123`
3. **Click:** "Sign In"
4. **Expected Result:**
   - ✅ Redirects to `/dashboard/`
   - ✅ Success message: "Welcome back, testuser!"
   - ✅ Dashboard shows user info

### 3. Test Signup Flow

1. **Logout first** (click Sign Out from dashboard)
2. **Visit:** `http://localhost:8000/auth/signup/`
3. **Enter:**
   - Username: `newuser` (or any unique username)
   - Password: `securepass123`
   - Confirm Password: `securepass123`
4. **Click:** "Create Account"
5. **Expected Result:**
   - ✅ Account created
   - ✅ Auto-logged in
   - ✅ Redirects to `/dashboard/`
   - ✅ Success message: "Welcome, newuser! Your account has been created."

### 4. Test Logout Flow

1. **From dashboard,** click "Sign Out" in navbar
2. **Expected Result:**
   - ✅ Redirects to homepage `/`
   - ✅ Success message: "You have been logged out successfully."
   - ✅ Navbar shows "Login" button again

### 5. Test Google OAuth (Optional)

1. **Make sure** your Google credentials are in `.env`:
   ```
   GOOGLE_CLIENT_ID=your-client-id
   GOOGLE_CLIENT_SECRET=your-secret
   ```
2. **Visit:** `http://localhost:8000/auth/signup/` or `/auth/login/`
3. **Click:** "Sign up with Google" or "Continue with Google"
4. **Expected Result:**
   - ✅ Redirects to Google OAuth
   - ✅ After auth, creates account automatically
   - ✅ Redirects to `/dashboard/`

## 🔍 What Changed (FBV Conversion)

### Before (CBVs):
```python
class UserSignupView(CreateView):
    template_name = "users/signup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("dashboard")
    # ... complex inheritance and methods
```

### After (FBVs):
```python
def signup_view(request):
    """Handle user signup."""
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            messages.success(request, f"Welcome, {user.username}!")
            return redirect("dashboard")
    else:
        form = UserCreationForm()

    return render(request, "users/signup.html", {"form": form})
```

**Benefits:**
- ✅ Cleaner and easier to understand
- ✅ More explicit control flow
- ✅ Easier to debug
- ✅ Less magic/inheritance complexity

## 📁 File Structure

```
users/
├── views.py              # Clean FBVs (signup, login, logout)
├── urls.py               # URL patterns
└── templates/users/
    ├── login.html        # Login page with username/password
    ├── signup.html       # Signup page with username/password
    └── dashboard.html    # User dashboard (requires login)
```

## 🔐 How Authentication Works

### Signup Flow:
1. User fills form → POST to `/auth/signup/`
2. `signup_view()` validates form
3. If valid: create user → log in → redirect to dashboard
4. If invalid: show errors on same page

### Login Flow:
1. User fills form → POST to `/auth/login/`
2. `login_view()` validates credentials with `AuthenticationForm`
3. If valid: authenticate → log in → redirect to dashboard
4. If invalid: show error

### Logout Flow:
1. User clicks "Sign Out" → GET to `/auth/logout/`
2. `logout_view()` logs out user
3. Redirect to homepage with message

## 🐛 Troubleshooting

### "No such table" error?
```bash
python manage.py migrate
```

### Form not submitting?
- Check that Tailwind is running (`npm run dev`)
- Check browser console for JavaScript errors
- Verify CSRF token is present in form

### Can't login after signup?
- Make sure password meets requirements (8+ chars)
- Check that username doesn't already exist
- Try the test user: `testuser` / `testpass123`

### Google OAuth not working?
1. Check credentials in `.env`
2. Verify redirect URIs in Google Console:
   ```
   http://localhost:8000/accounts/google/login/callback/
   ```
3. Check Site domain in Django admin

## 🎯 URLs Quick Reference

| URL | Purpose | Method | Auth Required |
|-----|---------|--------|---------------|
| `/` | Homepage | GET | No |
| `/auth/login/` | Login page | GET/POST | No |
| `/auth/signup/` | Signup page | GET/POST | No |
| `/auth/logout/` | Logout | GET | Yes |
| `/dashboard/` | User dashboard | GET | Yes |
| `/accounts/google/login/` | Google OAuth | GET | No |

## ✨ Features Working

- ✅ Username/password signup
- ✅ Username/password login
- ✅ Google OAuth login
- ✅ Auto-login after signup
- ✅ Logout with message
- ✅ Form validation and error display
- ✅ Success messages for all actions
- ✅ Redirect authenticated users away from login/signup
- ✅ Protected dashboard (login required)
- ✅ Clean white theme
- ✅ Responsive design
- ✅ Beautiful UI with Tailwind CSS

## 🚀 Next Steps

1. **Test everything** using the flows above
2. **Create more users** via signup
3. **Customize dashboard** in `users/templates/users/dashboard.html`
4. **Add more features** like password reset, profile editing, etc.

---

**Happy Testing!** 🎉

If you encounter any issues, check the terminal for Django errors and browser console for JavaScript errors.
