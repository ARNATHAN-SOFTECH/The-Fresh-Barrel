from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("verify/", views.verify, name="verify"),
    path("check-mobile/", views.check_mobile, name="check_mobile"),
]





