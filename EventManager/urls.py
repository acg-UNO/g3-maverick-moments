from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('events/', views.events, name='events'),
    path('events/<id>/', views.eventdetails, name='eventdetails'),
    path('events/register/<id>/', views.eventregister, name='eventregister'),
    path('events/unregister/<id>/', views.eventunregister, name='eventunregister'),

    path('venues/', views.venues, name='venues'),
    path('venues/<id>/', views.venuedetails, name='venuedetails'),

    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),

    path('venue/add', views.addvenue, name='addvenue'),
    path('venues/edit/<id>/', views.editvenuedetails, name='editvenue'),
    path('venues/delete/<id>/', views.deletevenue, name='deletevenue'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('events/', views.events, name='events'),
    path('events/add/', views.add_event, name='add_event'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/<int:event_id>/edit/', views.edit_event, name='edit_event'),
    ]
