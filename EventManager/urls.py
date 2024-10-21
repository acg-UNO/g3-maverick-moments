from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('venues/', views.venues, name='venues'),
    path('log_in_register/', views.log_in_register, name='log_in_register'),
    
]