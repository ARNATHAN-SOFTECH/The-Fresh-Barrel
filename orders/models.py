# orders/models.py

from django.db import models
from django.contrib.auth.models import User

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=15)

    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True)
    landmark = models.CharField(max_length=255, blank=True)

    pincode = models.CharField(max_length=10)
    locality = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)