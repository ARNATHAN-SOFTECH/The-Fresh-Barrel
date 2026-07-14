import random

from django.conf import settings
from django.core.mail import send_mail


def generate_otp():
    """
    Generate a random 6-digit OTP.
    """
    return str(random.randint(100000, 999999))


def send_otp(email, otp):
    """
    Send OTP to the user's email.
    """

    subject = "Your OTP for The Fresh Barrel"

    message = f"""
Hello,

Your One-Time Password (OTP) for The Fresh Barrel is:

{otp}

This OTP is valid for 5 minutes.

If you did not request this OTP, please ignore this email.

Thank you,

The Fresh Barrel Team
"""

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )

    return True