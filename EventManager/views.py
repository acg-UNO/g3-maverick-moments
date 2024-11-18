from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
    try: venue = get_object_or_404(Venue, id=id)
    except:
        messages.error(request, "venue not found")
        return redirect('venues')
    upcoming_events = Event.objects.filter(venue=venue, start_date__gte=timezone.now()).order_by('start_date')
    context = {
        'venue': venue,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'EventManager/venuedetails.html', context)

def addvenue(request):
    user = request.user
    if not user.is_superuser:
        return redirect('venuedetails', id)
    if request.method == 'POST':
        form = VenueDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            venue = form.save()
            messages.success(request, ("venue added successfully"))
            return redirect('venuedetails', venue.id)
    form = VenueDetailsForm()
    context = {
        'form': form,
    }
    return render(request, 'SuperUser/addvenue.html', context=context)

#edit venue
def editvenuedetails(request, id):
    user = request.user
    if not user.is_superuser:
        return redirect('venuedetails', id)
    try: venue = get_object_or_404(Venue, id=id)
    except: 
        messages.error(request, "venue not found")
        return redirect('venues')
    if request.method == 'POST':
        form = VenueDetailsForm(request.POST, request.FILES, instance=venue)
        if form.is_valid():
            form.save()
            messages.success(request, ("venue saved"))
            return redirect('venuedetails', id)
    form = VenueDetailsForm(instance = venue)
    context = {
        'form': form,
        'venue': venue
    }
    return render(request, 'SuperUser/editvenuedetails.html', context=context)

#delete a given venue
def deletevenue(request, id):
    user = request.user
    if not user.is_superuser:
        return redirect('venuedetails', id)
    try: venue = get_object_or_404(Venue, id=id)
    except: return redirect('venues')
    try:
        venue.delete()
        messages.success(request, "venue deleted successfully")
        return redirect('venues')
    except:
        messages.error(request, "unable to delete venue")
        return redirect('venuedetials', id)

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
    #1: get all registratoins by the user. 2: get the IDs of the events. 3: get a list of the events using the IDs
    registrations = Registration.objects.filter(user=request.user)
    registration_event_ids = list(registrations.values_list("event", flat=True))
    registered_events = Event.objects.filter(id__in=registration_event_ids)
    #order by date
    events_list = registered_events.order_by('start_date')
    context = {
        'events': events_list,
    }
    return render(request, "EventManager/account.html", context=context)

def add_event(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = EventForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('events')
        else:
            form = EventForm()
        return render(request, 'EventManager/add_event.html', {'form': form})
    else:
        return redirect('events')

def edit_event(request, id):
    if request.user.is_superuser:
        event = get_object_or_404(Event, id=id)
        if request.method == 'POST':
            form = EventForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                return redirect('eventdetails', id=id)
        else:
            form = EventForm(instance=event)
        return render(request, 'EventManager/edit_event.html', {'form': form, 'event': event})
    else:
        return redirect('events')
def deleteevent(request, id):
    user = request.user
    if not user.is_superuser:
        return redirect('eventdetails', id)
    try: venue = get_object_or_404(Venue, id=id)
    except: return redirect('events')
    try:
        venue.delete()
        messages.success(request, "event deleted successfully")
        return redirect('events')
    except:
        messages.error(request, "unable to delete event")
        return redirect('eventdetails', id)

def event_details(request, id):
    event = get_object_or_404(Event, id=id)
    registrations = Registration.objects.filter(event=event)

    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('eventdetails', id=id)  # Stay on the details page after editing
    else:
        form = EventForm(instance=event)

    return render(request, 'EventManager/eventdetails.html', {
        'event': event,
        'registrations': registrations,
        'form': form,
    })
def delete_registration(request, id):
    registration = get_object_or_404(Registration, id=id)
    event_id = registration.event.id
    registration.delete()
    return redirect('eventdetails', id=event_id)

# allows users to delete their own comments, requires login.
@login_required
def delete_comment(request, comment_id):
    # get the comment by id
    comment = get_object_or_404(EventComment, comment_id=comment_id)

    # checks to make sure it is original author and can delete the comment
    if request.user == comment.user:
        comment.delete()
        messages.success(request, "Comment deleted")
    else:
        messages.error(request, "You are not authorized to delete this comment.")

    return redirect('eventdetails', id=comment.event.id)
