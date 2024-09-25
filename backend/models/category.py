from django.db import models

class Category(models.Model):
    category_name = models.TextField(max_length=255, unique=True)
    description = models.TextField()
    category_thumbnail = models.ImageField(upload_to='category_thumbnail', null=True, blank=True)

    def __str__(self):
        return self.category_name