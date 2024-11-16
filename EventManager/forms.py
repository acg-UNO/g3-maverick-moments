from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import EventComment, Venue
from .models import Event
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes

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
<<<<<<< Updated upstream
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your comment...'}),
        }

class VenueDetailsForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'image', 'description', 'address_line_1', 'address_line_2', 'city', 'state', 'country', 'zipcode']
=======
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Enter your comment...'})

        }


class VenueDetailsForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'image', 'description', 'address_line_1', 'address_line_2', 'city', 'state', 'country',
                  'zipcode']

>>>>>>> Stashed changes

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
<<<<<<< Updated upstream
        fields = ['name', 'description', 'date']
=======

        fields = ['name', 'description', 'date']
>>>>>>> Stashed changes
