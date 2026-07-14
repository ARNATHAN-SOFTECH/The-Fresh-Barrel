from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse

from .models import Profile
from .utils import send_otp, generate_otp


def register(request):
    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        place = request.POST.get("place", "").strip()
        email = request.POST.get("email", "").strip().lower()

        if not email:
            messages.error(request, "Please enter a valid email address.")
            return redirect("register")

        existing_user = User.objects.filter(email=email).exists()

        if not existing_user:
            if not name or not place:
                messages.error(request, "Please enter your name and place.")
                return redirect("register")

        try:
            otp = generate_otp()

            send_otp(email, otp)

            request.session["otp"] = otp
            request.session["email"] = email
            request.session["name"] = name
            request.session["place"] = place

            messages.success(request, "OTP sent successfully.")

            return render(
                request,
                "accounts/verify_otp.html",
                {"email": email},
            )

        except Exception as e:
            messages.error(request, f"Failed to send OTP: {e}")
            return redirect("register")

    return render(request, "accounts/register.html")


def verify(request):
    if request.method != "POST":
        return redirect("register")

    entered_otp = request.POST.get("otp")
    saved_otp = request.session.get("otp")

    email = request.session.get("email")
    name = request.session.get("name")
    place = request.session.get("place")

    if not email:
        messages.error(request, "Session expired. Please register again.")
        return redirect("register")

    if str(entered_otp) != str(saved_otp):
        messages.error(request, "Invalid OTP.")
        return render(
            request,
            "accounts/verify_otp.html",
            {"email": email},
        )

    # ==========================
    # Existing User Login
    # ==========================
    if User.objects.filter(email=email).exists():

        user = User.objects.get(email=email)

        login(request, user)

        # Remove only OTP session data
        request.session.pop("otp", None)
        request.session.pop("email", None)
        request.session.pop("name", None)
        request.session.pop("place", None)

        messages.success(request, "Login Successful.")

        return redirect("dashboard")

    # ==========================
    # New User Registration
    # ==========================

    request.session["new_user_email"] = email
    request.session["new_user_name"] = name
    request.session["new_user_place"] = place

    return redirect("complete_profile")


@login_required
def complete_profile(request):

    if "new_user_email" not in request.session:
        messages.error(request, "Session expired.")
        return redirect("register")

    email = request.session.get("new_user_email")
    name = request.session.get("new_user_name")
    place = request.session.get("new_user_place")

    # Create User
    user, created = User.objects.get_or_create(
        username=email,
        defaults={
            "email": email,
        }
    )

    # Ensure email is correct
    if user.email != email:
        user.email = email
        user.save()

    # Create Profile
    profile, created = Profile.objects.get_or_create(
        user=user,
        defaults={
            "email": email,
            "name": name,
            "place": place,
            "is_email_verified": True,
        }
    )

    # Update existing profile
    if not created:
        profile.email = email
        profile.name = name
        profile.place = place
        profile.is_email_verified = True
        profile.save()

    login(request, user)

    # Remove only temporary registration session data
    request.session.pop("otp", None)
    request.session.pop("email", None)
    request.session.pop("name", None)
    request.session.pop("place", None)

    request.session.pop("new_user_email", None)
    request.session.pop("new_user_name", None)
    request.session.pop("new_user_place", None)

    messages.success(request, "Registration Successful.")

    return redirect("dashboard")


def check_email(request):
    email = request.GET.get("email", "").strip().lower()

    exists = User.objects.filter(email=email).exists()

    return JsonResponse({
        "exists": exists
    })

@login_required
def dashboard(request):

    profile, created = Profile.objects.get_or_create(
        user=request.user,
        defaults={
            "email": request.user.email
        }
    )

    context = {
        "profile": profile
    }

    return render(
        request,
        "accounts/dashboard.html",
        context
    )


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("home")