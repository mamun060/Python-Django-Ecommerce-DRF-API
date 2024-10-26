from rest_framework import serializers
from backend.models import Blog

class BlogSelializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'