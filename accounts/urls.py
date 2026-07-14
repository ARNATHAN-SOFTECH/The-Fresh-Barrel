from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("verify/", views.verify, name="verify"),
    path("check-email/", views.check_email, name="check_email"),

    path("complete-profile/", views.complete_profile, name="complete_profile"),
    path("dashboard/", views.dashboard, name="dashboard"),

    path("logout/", views.logout_view, name="logout"),
    path("login/", views.register, name="login"),
]