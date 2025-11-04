from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def index(request):
    """
    Homepage view.

    Redirects authenticated users to their dashboard,
    otherwise displays the landing page.
    """
    if request.user.is_authenticated:
        return redirect("dashboard")
    return render(request, "core/index.html")


@login_required
def dashboard(request):
    """
    User dashboard view.

    Requires authentication. Displays user's dashboard with
    profile information and quick actions.
    """
    return render(request, "core/dashboard.html")
