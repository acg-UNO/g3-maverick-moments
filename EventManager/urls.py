from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('events/', views.events, name='events'),
    path('events/<id>/', views.eventdetails, name='eventdetails'),
    path('events/register/<id>/', views.eventregister, name='eventregister'),

    path('venues/', views.venues, name='venues'),
    path('venues/<id>/', views.venuedetails, name='venuedetails'),

    path('register/', views.register, name='register'),
    ]
