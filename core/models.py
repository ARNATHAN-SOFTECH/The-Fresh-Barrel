from django.db import models
from django.utils.text import slugify


class Blog(models.Model):

    CATEGORY_CHOICES = (
        ('recipe', 'Recipe'),
        ('chicken', 'Chicken'),
        ('fish', 'Fish'),
        ('mutton', 'Mutton'),
        ('tips', 'Cooking Tips'),
        ('health', 'Health'),
    )

    title = models.CharField(max_length=250)

    slug = models.SlugField(unique=True, blank=True)

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    featured_image = models.ImageField(
        upload_to='blogs/'
    )

    excerpt = models.TextField(
        help_text="Small intro shown on blog page"
    )

    content = models.TextField()

    youtube_id = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    author = models.CharField(
        max_length=100,
        default="Fresh Barrel Team"
    )

    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title