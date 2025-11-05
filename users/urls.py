from django.urls import include, path

from . import views

app_name = "users"

urlpatterns = [
    # Authentication
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    # Profile Management
    path("settings/", views.SettingsView.as_view(), name="settings"),
    path("delete-account/", views.DeleteAccountView.as_view(), name="delete_account"),
    # Password Management (Django Allauth)
    # Note: Both "change password" and "reset password" use the same functionality
    # - "change password" = logged-in users changing their password
    # - "reset password" = forgot password flow via email
    path("password/", include("allauth.account.urls")),
]
