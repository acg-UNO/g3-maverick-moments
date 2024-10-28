from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('venues/', views.venues, name='venues'),
    path('register/', views.register, name='register'),
]
urlpatterns = [
    path('venues/<int:venue_id>/events/', views.venue_events, name='venue-events'),
    # other URL patterns
]