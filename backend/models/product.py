from django.utils.text import slugify
from django.db import models
from .category import Category
from .brand import Brand

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    product_title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)
    sub_title = models.CharField(max_length=255)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    color = models.JSONField()
    size = models.JSONField()
    product_thumbnail = models.ImageField(upload_to='product_thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.product_title)
        super().save(*args, **kwargs) 
    
    def __str__(self):
        return self.product_title
