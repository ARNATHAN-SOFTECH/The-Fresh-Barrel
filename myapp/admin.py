from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'name'
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'category',
        'price',
        'stock'
    ]

    list_filter = [
        'category'
    ]

    search_fields = [
        'name'
    ]


admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Tracking)