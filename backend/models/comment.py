from django.db import models
from . import Blog

class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"