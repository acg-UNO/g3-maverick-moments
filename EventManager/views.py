from django.shortcuts import render, get_object_or_404, redirect

from .models import *
import datetime


# Create your views here.
def index(request):
    context = None
    return render(request, 'EventManager/index.html', context=context)


def events(request):
    return render(request, 'EventManager/events.html')


def venues(request):
    return render(request, 'EventManager/venues.html')


def log_in_register(request):
    return render(request, 'EventManager/log_in_register.html')
