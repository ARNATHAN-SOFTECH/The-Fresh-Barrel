from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('fish/', views.fish, name='fish'),
    path('poultry/', views.poultry, name='poultry'),
    path('mutton/', views.mutton, name='mutton'),
]