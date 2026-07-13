from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('login/', views.login_view, name='login'),
    path('create-account/', views.create_account, name='create_account'),
    path('order-confirmation/', views.order_confirmation, name='order_confirmation'),
]