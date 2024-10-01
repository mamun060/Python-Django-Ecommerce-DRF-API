from django.db import models
from backend.models import Customer , Cart, Product

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.product_title}"
    
    def get_cart_total(self):
        return sum(item.get_total_price() for item in self.items.all())