from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required as need_login
from .apps.tasks.models import ClassProfile


@need_login
def index(request: HttpRequest) -> HttpResponse:
    """Main Page"""

    return render(request=request, template_name="index.html")


@need_login
def logout(request: HttpRequest) -> HttpResponse:
    """Log Out and Redirect to the Login Page"""

    auth_logout(request=request)

    return redirect(to="login")


"""def register_page(request: HttpRequest) -> HttpResponse:
    return render(request=request, template_name="create_user.html")


def register(request: HttpRequest) -> HttpResponse:
    ClassProfile.objects.create_user(username="2B", password="Bp081p")
    ClassProfile.objects.create_user(username="2C", password="omrCRO")
    ClassProfile.objects.create_user(username="3A", password="lvdAAj")
    ClassProfile.objects.create_user(username="3B", password="lp8MWc")

    if request.method == "POST":
        username = request.POST.get("ID")
        password = request.POST.get("password")

        if username and password:
            ClassProfile.objects.create_user(username=username, password=password)

            return redirect("login")

    return redirect("register")"""
