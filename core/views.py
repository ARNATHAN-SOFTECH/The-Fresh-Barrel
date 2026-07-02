from django.shortcuts import render
from products.models import Category


def home(request):
    categories = Category.objects.all()
    return render(request, 'core/home.html', {'categories': categories})


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