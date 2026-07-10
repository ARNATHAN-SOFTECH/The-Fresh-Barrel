from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login

from .models import Profile
from .utils import send_otp, verify_otp


def register(request):

    if request.method == "POST":

        name = request.POST.get("name")
        place = request.POST.get("place")
        mobile = request.POST.get("mobile")

        phone = "+91" + mobile

        # Check if mobile is already registered
        if User.objects.filter(username=mobile).exists():
            messages.error(request, "Mobile number is already registered.")
            return redirect("register")

        try:
            status = send_otp(phone)

            if status == "pending":

                request.session["name"] = name
                request.session["place"] = place
                request.session["mobile"] = mobile

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

        except Exception as e:
            messages.error(request, str(e))

    return render(request, "accounts/register.html")


from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect

from .models import Profile
from .utils import verify_otp


def verify(request):

    if request.method == "POST":

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

            if status == "approved":

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

                messages.success(request, "Registration Successful!")

                return redirect("home")

            else:

                messages.error(request, "Invalid OTP. Please try again.")

                return render(
                    request,
                    "accounts/verify_otp.html",
                    {"mobile": mobile}
                )

        except Exception:

            messages.error(request, "OTP verification failed.")

            return render(
                request,
                "accounts/verify_otp.html",
                {"mobile": mobile}
            )

    return render(request, "accounts/verify_otp.html")