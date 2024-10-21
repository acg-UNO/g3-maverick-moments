from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import *
import datetime


# Create your views here.
def index(request):
    context = None
    return render(request, 'EventManager/index.html', context=context)


def events(request):
    return render(request, 'EventManager/events.html')


def venues(request):
    return render(request, 'EventManager/venues.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') #change to login

        return redirect("register")
    else:
        form = RegisterForm()

    return render(request, "EventManager/register.html", {"form": form})
