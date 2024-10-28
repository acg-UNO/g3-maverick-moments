from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
import datetime
from .models import Event, EventComment
from .forms import EventCommentForm
from django.contrib.auth.decorators import login_required

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

# Event Details View
def eventdetails(request, id):
    id = int(id)
    try:
        event = Event.objects.get(id = id)
    except Event.DoesNotExist:
        return redirect('events')

    # get comments and add to context
    comments = event.eventcomment_set.all()

    # add form submission for adding comments to events (users must be logged in to add comments)
    if request.method == 'POST' and request.user.is_authenticated:
        form = EventCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user # makes user/comment association
            comment.event = event
            comment.save() # save comment to dbs
            return redirect('eventdetails', id=event.id)
    else:
        form = EventCommentForm() # makes it so it creates an empty form for GET request

    context = {
        'event': event,
        'comments': comments,
        'form': form
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
def venue_events(request, venue_id):
    venue = get_object_or_404(Venue, id=venue_id)
    upcoming_events = Event.objects.filter(venue=venue, date__gte=datetime.now()).order_by('date')
    context = {
        'venue': venue,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'EventManager/venue_events.html', context)