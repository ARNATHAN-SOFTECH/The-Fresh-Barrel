from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = [
        'id',
        'name'
    ]


from django.contrib import admin
from .models import Category, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "selling_price",
        "stock",
        "deal_of_the_day",
        "is_available",
    )

    list_filter = (
        "category",
        "deal_of_the_day",
        "is_available",
    )

    list_editable = (
        "deal_of_the_day",
        "is_available",
    )

    search_fields = ("name",)


admin.site.register(Profile)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Tracking)