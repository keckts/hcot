from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import UpdateView

from .forms import ProfileForm
from .models import Profile


def signup_view(request):
    """Handle user signup."""
    # Redirect if already authenticated
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Create the user
            user = form.save()

            # Log the user in
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")

            # Success message
            messages.success(request, f"Welcome, {user.username}! Your account has been created.")

            # Redirect to dashboard
            return redirect("dashboard")
    else:
        form = UserCreationForm()

    return render(request, "users/signup.html", {"form": form})


def login_view(request):
    """Handle user login."""
    # Redirect if already authenticated
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Get username and password from form
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            # Authenticate user
            user = authenticate(username=username, password=password)

            if user is not None:
                # Log the user in
                login(request, user)

                # Success message
                messages.success(request, f"Welcome back, {username}!")

                # Redirect to dashboard
                return redirect("dashboard")
    else:
        form = AuthenticationForm()

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
