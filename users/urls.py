from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", views.logout_view, name="logout"),
    path("settings/", views.SettingsView.as_view(), name="settings"),
    path("delete-account/", views.DeleteAccountView.as_view(), name="delete_account"),
]
