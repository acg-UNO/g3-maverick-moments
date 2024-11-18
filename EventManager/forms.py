from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import EventComment, Venue
from .models import Event

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]


class EventCommentForm(forms.ModelForm):
    class Meta:
        model = EventComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your comment...'}),
        }

class VenueDetailsForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'image', 'description', 'address_line_1', 'address_line_2', 'city', 'state', 'country', 'zipcode']

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['description','title', 'description', 'start_date', 'end_date', 'venue', 'image']

