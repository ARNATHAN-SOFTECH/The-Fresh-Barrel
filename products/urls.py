from django.urls import path
from . import views

urlpatterns = [
    path(
        'category/<int:pk>/',
        views.category_products,
        name='category_products'
    ),

    path(
        'product/<int:pk>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        'add-to-cart/<int:product_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/',
        views.cart,
        name='cart'
    ),

    path(
        'increase-cart/<int:product_id>/',
        views.increase_cart,
        name='increase_cart'
    ),

    path(
        'decrease-cart/<int:product_id>/',
        views.decrease_cart,
        name='decrease_cart'
    ),

    path(
        'remove-cart/<int:product_id>/',
        views.remove_cart,
        name='remove_cart'
    )
]