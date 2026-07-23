from django.contrib.sitemaps import Sitemap
from django.urls import reverse


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = "daily"

    def items(self):
        return [
            "home",
        ]

    def location(self, item):
        return reverse(item)
    
from products.models import Product


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Product.objects.filter(is_available=True)

    def lastmod(self, obj):
        return obj.created_at