from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required

#About page
def index(request):
    context = None
    return render(request, 'EventManager/index.html', context=context)

#Events list page
def events(request):
    #get a list of future events and order by start_date
    events_list = Event.objects.filter(start_date__gte=timezone.now()).order_by('start_date') #change to end_date when adding default
    registered_events = None

    #if a user is logged in then get a list of events they are registered for
    if request.user.is_authenticated:
        #1: get all registratoins by the user. 2: get the IDs of the events. 3: get a list of the events using the IDs
        registrations = Registration.objects.filter(user=request.user)
        registration_event_ids = list(registrations.values_list("event", flat=True))
        registered_events = Event.objects.filter(id__in=registration_event_ids)

    context = {'events': events_list,
               'registered': registered_events}
    return render(request, 'EventManager/events.html', context)

# Event Details View
def eventdetails(request, id):
    registered = False

    #checks the event id is valid and redirects to events list if not
    try: event = Event.objects.get(id = id)
    except Event.DoesNotExist: return redirect('events')
    
    #if the user is registered for the event then registered = True. Checks if there's a registration object with the user and event
    if request.user.is_authenticated:
        try: 
            Registration.objects.get(user = request.user, event = event)
            registered = True
        except: pass

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
        'form': form,
        'registered': registered
    }
    return render(request, 'EventManager/eventdetails.html', context = context)

# This never returns an HTML page, and instead registers the user and redirects to the event details page.
def eventregister(request, id):
    if request.user.is_authenticated:
        try: event = Event.objects.get(id = id)
        except: return redirect('events')
        Registration.objects.create(user = request.user, event = event)
        return redirect('eventdetails', id)
    else:
        return redirect('login')
    
def eventunregister(request, id):
    if request.user.is_authenticated:
        try: event = Event.objects.get(id=id)
        except: return redirect('events')
        try: 
            instance = Registration.objects.get(event=event, user=request.user)
            instance.delete()
        except: pass
        return redirect('events')
    else:
        return redirect('login')

#List of venues
def venues(request):
    venues_list = Venue.objects.all()
    context = {'venues': venues_list}
    return render(request, 'EventManager/venues.html', context)

#Venue Details and future events
def venuedetails(request, id):
    venue = get_object_or_404(Venue, id=id)
    print()
    upcoming_events = Event.objects.filter(venue=venue, start_date__gte=timezone.now()).order_by('start_date')
    context = {
        'venue': venue,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'EventManager/venuedetails.html', context)

#Account creation
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        return redirect("register")
    else:
        form = RegisterForm()

    context = {
        'form': form
    }
    return render(request, "EventManager/register.html", context=context)

def account(request):
    user = request.user
    if not user.is_authenticated:
        return redirect("login")
    
    context = None
    return render(request, "EventManager/account.html", context=context)