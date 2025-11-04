# Django HCOT Boilerplate

**HCOT** stands for **HTMX + Cotton + Django** - A modern, production-ready Django boilerplate template.

Created by Henry Sheffield, this boilerplate provides a solid foundation for building modern web applications with Django, featuring email-based authentication, user profile management, and beautiful UI components.

## ✨ Features

- 🔐 **Email-Based Authentication** - Modern signup/login with email instead of username
- 👤 **User Profile Management** - Complete profile editing with bio, location, and birth date
- 🎨 **Beautiful UI** - TailwindCSS + DaisyUI for stunning, responsive design
- ⚡ **HTMX Integration** - Dynamic, modern interactions without writing JavaScript
- 🎭 **Django Cotton** - Component-based templating for cleaner code
- 🌓 **Dark Mode** - Built-in dark mode toggle that persists across sessions
- 🔒 **Security First** - CSRF protection, secure password handling, and more
- 📱 **Fully Responsive** - Works beautifully on all devices
- 🗑️ **Account Management** - Delete account functionality with confirmation modals
- ⚙️ **Settings Page** - Comprehensive user settings with profile editing
- 📊 **Dashboard** - Beautiful user dashboard with stats and quick actions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for cloning)

### Installation

1. **Clone or download the repository**

```bash
git clone <your-repo-url>
cd hcot
```

2. **Create and activate a virtual environment**

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Rename the project (IMPORTANT)**

Run the included rename script to customize the project name:

```bash
python rename_project.py yourprojectname
```

This will automatically:
- Rename the project directory
- Update all file references
- Update HTML templates
- Update configuration files

5. **Set up the database**

```bash
python manage.py migrate
```

6. **Create a superuser**

```bash
python manage.py createsuperuser
```

7. **Install and configure TailwindCSS + DaisyUI (for macOS)**

```bash
# Navigate to theme static CSS directory
cd theme/static/css

# Download DaisyUI and TailwindCSS
curl -sL daisyui.com/fast | bash

# Build CSS (run in a separate terminal to watch for changes)
./tailwindcss -i input.css -o dist/styles.css --watch
```

For other operating systems, download TailwindCSS from [https://tailwindcss.com/blog/standalone-cli](https://tailwindcss.com/blog/standalone-cli)

8. **Run the development server**

```bash
# In a new terminal (keep TailwindCSS watch running in another)
python manage.py runserver
```

9. **Open your browser**

Navigate to `http://127.0.0.1:8000/` and start building!

## 📁 Project Structure

```
yourprojectname/
├── core/                   # Core app (homepage, dashboard)
├── users/                  # User authentication & profiles
│   ├── templates/
│   │   └── users/
│   │       ├── login.html
│   │       ├── signup.html
│   │       └── settings.html
│   ├── forms.py           # Email-based auth forms
│   ├── models.py          # User Profile model
│   └── views.py           # Authentication views
├── theme/                  # Theme and base templates
│   ├── static/css/        # TailwindCSS configuration
│   └── templates/
│       └── theme/
│           └── base.html  # Base template with sidebar
├── yourprojectname/       # Project settings
│   ├── settings.py
│   └── urls.py
├── manage.py
├── rename_project.py      # Project renaming script
└── requirements.txt
```

## 🎨 Customization

### Changing the Project Name

Use the included rename script:

```bash
python rename_project.py mynewproject
```

### Customizing Styles

1. Edit `theme/static/css/input.css` for global styles
2. Modify DaisyUI theme in `theme/static/css/tailwind.config.js`
3. Use TailwindCSS utility classes directly in templates

### Adding New Features

1. Create new Django apps: `python manage.py startapp myapp`
2. Add app to `INSTALLED_APPS` in settings
3. Create models, views, and templates
4. Add URL patterns

## 🔧 Configuration

### Environment Variables

For production, create a `.env` file (see `.env.example`):

```env
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=your-database-url
```

### Email Backend (Optional)

Configure email settings in `settings.py` for:
- Password reset
- Email notifications
- User verification

### Social Authentication (Optional)

The boilerplate includes Google OAuth setup. Configure in `settings.py`:

1. Get OAuth credentials from Google Cloud Console
2. Add to `SOCIALACCOUNT_PROVIDERS` in settings
3. Update templates as needed

## 📝 Key Features Explained

### Email-Based Authentication

Users sign up and log in with email addresses instead of usernames. The system automatically uses email as the username internally for Django compatibility.

### Profile Management

Each user has an associated Profile model with:
- Bio
- Location
- Birth date
- Automatically created on user signup

### Dark Mode

Dark mode preference is stored in localStorage and persists across sessions. Toggle available in settings page.

### Settings Page

Comprehensive settings interface with:
- Profile editing
- Account information display
- Dark mode toggle
- Logout functionality
- Account deletion (with confirmation)

## 🛠️ Development

### Running Tests

```bash
python manage.py test
```

### Creating Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files (Production)

```bash
python manage.py collectstatic
```

## 📦 Dependencies

Key packages included:
- **Django 5.1.3** - Web framework
- **django-tailwind** - TailwindCSS integration
- **django-cotton** - Component-based templates
- **django-allauth** - Authentication & social auth
- **python-dotenv** - Environment variable management

See `requirements.txt` for complete list.

## 🤝 Contributing

Feel free to fork this project and customize it for your needs. If you make improvements, consider sharing them back!

## 📄 License

This project is provided as-is for use as a boilerplate template.

## 👨‍💻 Author

Created by **Henry Sheffield**

## 🙏 Acknowledgments

- Django community
- TailwindCSS team
- DaisyUI creators
- HTMX developers
- Django Cotton project

## 💡 Tips

1. **Always use the virtual environment** - Activate it before running any commands
2. **Keep TailwindCSS watch running** - During development for instant CSS updates
3. **Customize early** - Run the rename script before making changes
4. **Check migrations** - Run `makemigrations` and `migrate` after model changes
5. **Use the admin panel** - Access at `/admin` for easy data management

## 🆘 Troubleshooting

### TailwindCSS not updating
- Make sure the watch command is running
- Check that you're editing `input.css`, not `dist/styles.css`

### Database errors
- Delete `db.sqlite3` and run migrations again
- Check that all migrations are applied

### Import errors
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`

### Static files not loading
- Run `python manage.py collectstatic`
- Check `STATIC_URL` and `STATIC_ROOT` in settings

---

**Happy coding!** 🚀
