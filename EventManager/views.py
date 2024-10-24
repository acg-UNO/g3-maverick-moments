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

def eventdetails(request, id):
    id = int(id)
    try: event = Event.objects.get(id = id)
    except Event.DoesNotExist: return redirect('events')
    # get comments and add to context
    context = {
        'event': event
    }
    return render(request, 'EventManager/eventdetails.html', context = context)

def eventregister(request, id):
    id = int(id)
    try: event = Event.objects.get(id = id)
    except Event.DoesNotExist: return redirect('events')
    try: user = request.user
    except: return redirect('events')
    Registration.objects.create(user = user, event = event)
    return redirect('eventdetails', id)


def venues(request):
    venues_list = Venue.objects.all()
    context = {'venues': venues_list}
    return render(request, 'EventManager/venues.html', context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index') #change to login

        return redirect("register")
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, "EventManager/register.html", context=context)
