
from django.shortcuts import render
from .models import Product


def fish(request):

    products = Product.objects.filter(
        category__name='Fish'
    )

    return render(
        request,
        'fish.html',
        {
            'products': products
        }
    )




from django.shortcuts import render
from .models import Product


def poultry(request):

    products = Product.objects.filter(
        category__name__iexact='Poultry'
    )

    return render(
        request,
        'poultry.html',
        {
            'products': products
        }
    )

def mutton(request):

    products = Product.objects.filter(
        category__name='Mutton'
    )

    return render(
        request,
        'mutton.html',
        {
            'products': products
        }
    )
def faq(request):
    return render(request, 'faq.html')

def terms_conditions(request):
    return render(request, 'terms_conditions.html')

def blog(request):
    return render(request, 'blog.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def refund_policy(request):
    return render(request, 'refund_policy.html')

def contact_us(request):
    return render(request, 'contact_us.html')