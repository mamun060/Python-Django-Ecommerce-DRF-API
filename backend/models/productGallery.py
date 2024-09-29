from django.db import models
from .product import Product

class ProductGallery(models.Model):
    product = models.ForeignKey(Product, related_name="galleries", on_delete=models.CASCADE)
    gallery_image = models.FileField(upload_to="product_gallery/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Gallery for {self.product.product_title}" if self.product else "Gallery without a product"