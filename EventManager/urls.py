from django.urls import path
from . import views

urlpatterns = [
    # Index and Event URLs

    #basic user event pages
    path('', views.index, name='index'),
    path('events/', views.events, name='events'),
    path('events/<int:id>/', views.eventdetails, name='eventdetails'),

    #superuser event controls
    path('events/add/', views.add_event, name='add_event'),
    path('events/<int:id>/edit/', views.edit_event, name='edit_event'),
    path('events/<int:id>/delete/', views.deleteevent, name='deleteevent'),

    #registrations
    path('events/register/<int:id>/', views.eventregister, name='eventregister'),
    path('events/unregister/<int:id>/', views.eventunregister, name='eventunregister'),
    path('delete_registration/<int:id>/', views.delete_registration, name='delete_registration'), #superuser


    # Venue URLs

    #basic user venue pages
    path('venues/', views.venues, name='venues'),
    path('venues/<int:id>/', views.venuedetails, name='venuedetails'),

    #superuser venue controls
    path('venues/add/', views.addvenue, name='addvenue'),
    path('venues/<int:id>/edit/', views.editvenuedetails, name='editvenue'),
    path('venues/<int:id>/delete/', views.deletevenue, name='deletevenue'),


    # Account and Registration
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('editaccount/', views.editaccount, name='editaccount'),

    # Comments
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
