from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "place",
        "is_email_verified",
        "created_at",
    )

    list_filter = (
        "is_email_verified",
    )

    search_fields = (
        "name",
        "email",
        "place",
    )