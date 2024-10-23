from django.contrib import admin
from .models import *

# allows addition/modification of venues via /admin
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Registration)
admin.site.register(EventComment)
