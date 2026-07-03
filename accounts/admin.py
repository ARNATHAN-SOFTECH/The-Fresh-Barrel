from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'mobile',
        'place',
        'is_mobile_verified',
        'created_at',
    )

    search_fields = ('name', 'mobile', 'place')
    list_filter = ('is_mobile_verified',)