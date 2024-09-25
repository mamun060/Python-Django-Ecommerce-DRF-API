from django.db import models
from .category import Category

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    color = models.JSONField()  # Store multiple color options
    size = models.JSONField()  # Store multiple size options
    product_thumbnail = models.ImageField(upload_to='product_thumbnails/')
    product_gallery = models.JSONField()  # Store multiple image URLs for the gallery

    def __str__(self):
        return self.product_title
