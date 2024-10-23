from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('events/<pk>/', views.eventdetails, name='eventdetails'),
    path('venues/', views.venues, name='venues'),
    path('register/', views.register, name='register'),
]