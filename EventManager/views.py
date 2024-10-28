from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
import datetime
from .models import Event


# Create your views here.
def index(request):
    context = None
    return render(request, 'EventManager/index.html', context=context)


def events(request):
    events_list = Event.objects.all()
    context = {'events': events_list}
    return render(request, 'EventManager/events.html', context)


def event_list(request):
    events = Event.objects.all().order_by('title', 'start_date')
    return render(request, 'EventManager/event_list.html', {'events': events})


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


def maverick_moments(request):
    return render(request, 'EventManager/base.html', context)


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
