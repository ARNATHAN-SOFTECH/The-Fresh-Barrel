from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login

from .models import Profile
from .utils import send_otp, verify_otp


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

from .utils import send_otp


def register(request):

    if request.method == "POST":

        # Get form data
        name = request.POST.get("name", "").strip()
        place = request.POST.get("place", "").strip()
        mobile = request.POST.get("mobile", "").strip()

        # Validate mobile number
        if len(mobile) != 10 or not mobile.isdigit():

            messages.error(request, "Please enter a valid 10-digit mobile number.")
            return redirect("register")

        # Check if the mobile number already exists
        existing_user = User.objects.filter(username=mobile).exists()

        # Name and Place are required only for new users
        if not existing_user:

            if not name or not place:

                messages.error(request, "Please enter your name and place.")
                return redirect("register")

        phone = "+91" + mobile

        try:

            status = send_otp(phone)

            if status == "pending":

                # Save data in session
                request.session["mobile"] = mobile
                request.session["name"] = name
                request.session["place"] = place

                messages.success(request, "OTP sent successfully.")

                return render(
                    request,
                    "accounts/verify_otp.html",
                    {
                        "mobile": mobile
                    }
                )

            else:

                messages.error(request, "Unable to send OTP.")
                return redirect("register")

        except Exception as e:

            messages.error(request, str(e))
            return redirect("register")

    return render(request, "accounts/register.html")


def verify(request):

    if request.method != "POST":

        return redirect("register")

    otp = request.POST.get("otp")

    mobile = request.session.get("mobile")
    name = request.session.get("name")
    place = request.session.get("place")

    if not mobile:

        messages.error(request, "Session expired. Please register again.")

        return redirect("register")

    phone = "+91" + mobile

    try:

        status = verify_otp(phone, otp)

        if status != "approved":

            messages.error(request, "Invalid OTP.")

            return render(
                request,
                "accounts/verify_otp.html",
                {
                    "mobile": mobile
                }
            )

        # ------------------------------
        # USER EXISTS → LOGIN
        # ------------------------------

        if User.objects.filter(username=mobile).exists():

            user = User.objects.get(username=mobile)

            login(request, user)

            # Clear session
            request.session.pop("name", None)
            request.session.pop("place", None)
            request.session.pop("mobile", None)

            messages.success(request, "Login Successful.")

            return redirect("home")

        # ------------------------------
        # NEW USER → REGISTER
        # ------------------------------

        user = User.objects.create_user(
            username=mobile
        )

        Profile.objects.create(
            user=user,
            name=name,
            place=place,
            mobile=mobile,
            is_mobile_verified=True
        )

        login(request, user)

        # Clear session
        request.session.pop("name", None)
        request.session.pop("place", None)
        request.session.pop("mobile", None)

        messages.success(request, "Registration Successful.")

        return redirect("home")

    except Exception as e:

        messages.error(request, str(e))

        return render(
            request,
            "accounts/verify_otp.html",
            {
                "mobile": mobile
            }
        )
    


from django.http import JsonResponse
from django.contrib.auth.models import User


def check_mobile(request):

    mobile = request.GET.get("mobile")

    exists = User.objects.filter(username=mobile).exists()

    return JsonResponse({
        "exists": exists
    })






from django.contrib.auth import logout


def logout_view(request):

    logout(request)

    return redirect("home")