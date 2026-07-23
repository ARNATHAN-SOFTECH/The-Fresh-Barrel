from django.shortcuts import render
from products.models import Product, Category
from django.shortcuts import get_object_or_404

def home(request):

    seo = {
        "title": "The Fresh Barrel | Fresh Fish, Chicken & Mutton",
        "description": "Order fresh fish, seafood, chicken and mutton online with hygienic cleaning and fast doorstep delivery.",
        "keywords": "fresh fish, seafood, chicken, mutton, online fish delivery",
        "url": request.build_absolute_uri(),
        "canonical": request.build_absolute_uri(),
        "image": request.build_absolute_uri("/static/img/logo.jpeg"),
        "type": "website",
        "site_name": "The Fresh Barrel",
        "twitter_card": "summary_large_image",
    }

    deals = Product.objects.filter(
        deal_of_the_day=True,
        is_available=True
    )

    categories = Category.objects.all()

    return render(
        request,
        "core/home.html",
        {
            "seo": seo,
            "deals": deals,
            "categories": categories,
        },
    )

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


# core/views.py

from .models import Blog


def blog_list(request):

    blogs = Blog.objects.filter(
        is_published=True
    ).order_by('-created_at')

    return render(
        request,
        'core/blog.html',
        {'blogs': blogs}
    )


def blog_detail(request, slug):

    blog = get_object_or_404(
        Blog,
        slug=slug,
        is_published=True
    )

    return render(
        request,
        'core/blog_detail.html',
        {'blog': blog}
    )


from django.http import HttpResponse


def robots_txt(request):
    return HttpResponse(
        """User-agent: *

Allow: /

Disallow: /admin/
Disallow: /accounts/
Disallow: /cart/
Disallow: /checkout/

Sitemap: https://thefreshbarrel.in/sitemap.xml
""",
        content_type="text/plain",
    )