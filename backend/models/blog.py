from django.db import models
from . import Author 

class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='blog_thumbnails/', null=True, blank=True)

    def __str__(self):
        return self.title