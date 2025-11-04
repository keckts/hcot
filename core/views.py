from django.shortcuts import redirect, render


def index(request):
    """Homepage - redirects authenticated users to dashboard."""
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "core/index.html")


def dashboard(request):
    return render(request, "core/dashboard.html", {"user": request.user})
