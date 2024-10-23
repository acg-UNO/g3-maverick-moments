from django.contrib import admin
from .models import Venue

# allows addition/modification of venues via /admin
admin.site.register(Venue)