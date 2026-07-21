
from django.shortcuts import render
from products.models import Product, Category

def home(request):
    deals = Product.objects.filter(
        deal_of_the_day=True,
        is_available=True
    )

    categories = Category.objects.all()

    print("Deals Count:", deals.count())
    print("Categories Count:", categories.count())

    return render(request, "core/home.html", {
        "deals": deals,
        "categories": categories,
    })

def contact_us(request):
    return render(request, 'core/contact_us.html')


def faq(request):
    return render(request, 'core/faq.html')


def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')


def refund_policy(request):
    return render(request, 'core/refund_policy.html')


def terms_conditions(request):
    return render(request, 'core/terms_conditions.html')


def blog(request):
    return render(request, 'core/blog.html')