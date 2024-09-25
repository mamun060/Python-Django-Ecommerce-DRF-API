from django.db import models
from . import Customer

class Profile(models.Model):
    customerID = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email_id = models.EmailField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    dob = models.DateField(verbose_name="Date of Birth")
    location = models.CharField(max_length=255)
    customer_image = models.ImageField(upload_to='customer_images/', null=True, blank=True)

    def __str__(self):
        return self.full_name