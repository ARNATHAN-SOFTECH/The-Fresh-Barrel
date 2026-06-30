from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    path('fish/', views.fish, name='fish'),
    path('poultry/', views.poultry, name='poultry'),
    path('mutton/', views.mutton, name='mutton'),

    path('faq/', views.faq, name='faq'),
    path('terms-and-conditions/', views.terms_conditions, name='terms_conditions'),
    path('blog/', views.blog, name='blog'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('refund-policy/', views.refund_policy, name='refund_policy'),
    path('contact-us/', views.contact_us, name='contact_us'),
]