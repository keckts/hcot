from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from .forms import EmailLoginForm, EmailSignupForm, ProfileForm
from .models import Profile


def signup_view(request):
    """Handle user signup with email."""
    # Redirect if already authenticated
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = EmailSignupForm(request.POST)
        if form.is_valid():
            # Create the user
            user = form.save()

            # Log the user in
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")

            # Success message
            messages.success(request, f"Welcome! Your account has been created.")

            # Redirect to dashboard
            return redirect("dashboard")
    else:
        form = EmailSignupForm()

    return render(request, "users/signup.html", {"form": form})


def login_view(request):
    """Handle user login with email."""
    # Redirect if already authenticated
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            # Get email and password from form
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            # Get user by email
            try:
                user_obj = User.objects.get(email=email)
                # Authenticate using username (which is set to email)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

            if user is not None:
                # Log the user in
                login(request, user)

                # Success message
                messages.success(request, "Welcome back!")

                # Redirect to dashboard
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = EmailLoginForm()

    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    """Handle user logout."""
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("index")


class SettingsView(LoginRequiredMixin, UpdateView):
    """View for user settings and profile editing."""

    model = Profile
    form_class = ProfileForm
    template_name = "users/settings.html"
    success_url = reverse_lazy("users:settings")

    def get_object(self, queryset=None):
        """Get or create the profile for the current user."""
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        """Handle successful form submission."""
        messages.success(self.request, "Your profile has been updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        """Handle invalid form submission."""
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)


class DeleteAccountView(LoginRequiredMixin, View):
    """View for deleting user account."""

    def post(self, request):
        """Handle account deletion."""
        user = request.user
        username = user.username

        # Logout and delete the user
        logout(request)
        user.delete()

        # Success message
        messages.success(request, f"Account '{username}' has been permanently deleted.")

        # Redirect to index
        return redirect("index")
