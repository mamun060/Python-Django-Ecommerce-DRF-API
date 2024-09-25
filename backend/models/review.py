from django.db import models
from .customer import Customer
from .product import Product

class Review(models.Model):
    start = models.PositiveIntegerField()  # Rating
    review_text = models.TextField()
    userID = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"Review for {self.product.product_title} by {self.userID.name}: {self.review_text[:20]}"
