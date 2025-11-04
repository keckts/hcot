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
    """
    User signup view with email-based authentication.

    GET: Display signup form
    POST: Process signup form, create user, and log them in

    Redirects authenticated users to dashboard.
    """
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = EmailSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            messages.success(request, "Welcome! Your account has been created.")
            return redirect("dashboard")
    else:
        form = EmailSignupForm()

    return render(request, "users/signup.html", {"form": form})


def login_view(request):
    """
    User login view with email-based authentication.

    GET: Display login form
    POST: Authenticate user by email and password, then log them in

    Redirects authenticated users to dashboard.
    """
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")

            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

            if user is not None:
                login(request, user)
                messages.success(request, "Welcome back!")
                return redirect("dashboard")
            else:
                messages.error(request, "Invalid email or password.")
    else:
        form = EmailLoginForm()

    return render(request, "users/login.html", {"form": form})


def logout_view(request):
    """
    User logout view.

    Logs out the current user and redirects to homepage.
    """
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect("index")


class SettingsView(LoginRequiredMixin, UpdateView):
    """
    User settings and profile editing view.

    Allows authenticated users to view and update their profile information
    including name, email, bio, location, and birth date.
    """

    model = Profile
    form_class = ProfileForm
    template_name = "users/settings.html"
    success_url = reverse_lazy("users:settings")

    def dispatch(self, request, *args, **kwargs):
        # clear old messages
        storage = messages.get_messages(request)
        list(storage)  # Iterate through the storage to clear old messages
        storage.used = True

        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Get or create the profile for the current user.

        Returns:
            Profile: The user's profile object
        """
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        """
        Handle successful form submission.

        Args:
            form: The validated ProfileForm

        Returns:
            HttpResponse: Redirect to success URL
        """
        messages.success(self.request, "Your profile has been updated successfully!")
        return super().form_valid(form)

    def form_invalid(self, form):
        """
        Handle invalid form submission.

        Args:
            form: The invalid ProfileForm

        Returns:
            HttpResponse: Re-render form with errors
        """
        messages.error(self.request, "Please correct the errors below.")
        return super().form_invalid(form)


class DeleteAccountView(LoginRequiredMixin, View):
    """
    Account deletion view.

    Allows authenticated users to permanently delete their account
    and all associated data.
    """

    def post(self, request):
        """
        Handle account deletion request.

        Logs out the user, deletes their account, and redirects to homepage.

        Args:
            request: The HTTP request

        Returns:
            HttpResponse: Redirect to index page
        """
        user = request.user
        email = user.email

        logout(request)
        user.delete()

        messages.success(request, f"Account '{email}' has been permanently deleted.")
        return redirect("index")
