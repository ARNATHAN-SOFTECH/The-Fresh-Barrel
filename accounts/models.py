from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    name = models.CharField(max_length=100, blank=True)

    email = models.EmailField(unique=True)

    place = models.CharField(max_length=100, blank=True)

    is_email_verified = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name if self.name else self.email


class Address(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="addresses"
    )

    full_address = models.TextField()

    landmark = models.CharField(
        max_length=200,
        blank=True
    )

    pincode = models.CharField(
        max_length=10
    )

    mobile = models.CharField(
        max_length=15
    )

    is_default = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.user.username} - {self.mobile}"