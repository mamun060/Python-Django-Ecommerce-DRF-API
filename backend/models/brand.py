from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='brand', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name