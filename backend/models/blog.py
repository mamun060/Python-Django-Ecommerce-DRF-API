from django.db import models
from . import Author 
from django.utils.text import slugify

class Blog(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='blogs')
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255, blank=True, null=True)
    sub_title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='blog_thumbnails/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Auto-generate the slug based on the title
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title