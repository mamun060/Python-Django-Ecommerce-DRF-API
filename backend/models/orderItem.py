from django.db import models
from . import Order, Product

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=50)  # Size of the product
    color = models.CharField(max_length=50)  # Color of the product
    quantity = models.PositiveIntegerField()  # Quantity of the product
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.quantity} x {self.product.product_title} (Size: {self.size}, Color: {self.color})"