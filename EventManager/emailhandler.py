from django.core.mail import send_mail
from django.conf import settings

sender = settings.EMAIL_HOST_USER

def user_alert(type, user, event=None):
    match type:
        case 'register':
            subject = "registration confirmation"
            message = f"Hello, \n\n thanks for signing up for Mav Moments! \n Your username is {user.username}"
        case 'eventRegister':
            subject = f"Event Registration on {event.start_date}"
            message = f"This is a reminder that you have registered for {event.title} on {event.start_date} at {event.venue}. \n\n Event Details: {event.description}"
        case 'eventUnregister':
            subject = f"Event Unregistration Confirmation"
            message = f"this is an email confirmation that you have unregistered for {event.title}"

    receiver = [user.email]
    send_mail(
        subject,
        message,
        sender,
        receiver,
        fail_silently=False,
    )