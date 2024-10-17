from django.db import models
from django.contrib.auth.models import User

# Venue Model
class Venue(models.Model):
    name = models.CharField(max_length=200)
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='venue_images/', blank=True, null=True)

    def __str__(self):
        return self.name

# Event Model
class Event(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    description = models.TextField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return self.title

# Registration Model
class Registration(models.Model):
    registration_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


#Event Model
class EventComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    text = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
