from django.db import models
from django.utils import timezone
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products"
    )

    image = models.ImageField(upload_to="products/")

    description = models.TextField(blank=True)

    weight = models.CharField(
        max_length=50,
        default="500g"
    )

    original_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    selling_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    stock = models.IntegerField(default=0)

    is_available = models.BooleanField(default=True)

    deal_of_the_day = models.BooleanField(
        default=False,
        help_text="Show on Deal Of The Day section"
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        editable=False
    )

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name



