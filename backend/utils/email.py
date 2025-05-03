from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_password_reset_email(user, reset_url):
    """
    Send password reset email to user with reset link.
    
    Args:
        user: User instance who requested password reset
        reset_url: URL with token to reset password
    """
    context = {
        'user': user,
        'reset_url': reset_url,
    }
    
    html_message = render_to_string('emails/password_reset.html', context)
    plain_message = strip_tags(html_message)
    
    send_mail(
        subject='Password Reset Request',
        message=plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        html_message=html_message,
        fail_silently=False,
    ) 