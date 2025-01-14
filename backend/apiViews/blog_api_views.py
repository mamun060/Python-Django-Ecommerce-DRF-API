from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from backend.models import Blog
from backend.serializers import BlogSelializer

class BlogApiViews(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        blogs = Blog.objects.all()
        serializeBlog = BlogSelializer(blogs, many=True)
        return Response(
            serializeBlog.data,
            status=status.HTTP_200_OK
        )
    

class SingleBlogApiView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        serializer = BlogSelializer(blog)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )