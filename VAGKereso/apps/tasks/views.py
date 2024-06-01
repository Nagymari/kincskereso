from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required as need_login
from .models import Task


def get_object(name: str) -> str:
    """Give the answer to the task."""

    for item in Task.objects.all():
        if item.name == name:
            return item



@need_login
def kolto(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        answer = request.POST.get("answer")

        if answer:
            object = get_object("A költő")
            if answer == object.answer:
                request.user.add_task(object)
    else:
        return render(request, "kolto.html")
    return HttpResponse("Hello")


