from rest_framework import serializers
from backend.models import Comment


class CommentSelializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'