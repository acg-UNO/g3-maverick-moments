from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('events/<id>/', views.eventdetails, name='eventdetails'),
    path('venues/', views.venues, name='venues'),
    path('register/', views.register, name='register'),
    path('events/register/<id>/', views.eventregister, name='eventregister'),
    path('', views.event_list, name='event_list'),
    path('maverick_moments/', views.index, name= 'maverick_moments'),
    ]
