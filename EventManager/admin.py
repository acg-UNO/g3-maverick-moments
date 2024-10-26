from django.contrib import admin
from .models import *
from .models import Event

# allows addition/modification of venues via /admin
admin.site.register(Venue)
admin.site.register(Event)
admin.site.register(Registration)
admin.site.register(EventComment)


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'time')
    ordering = ('start_date', 'time')
