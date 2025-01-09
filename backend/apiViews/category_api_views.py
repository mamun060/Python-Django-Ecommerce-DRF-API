from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.models import Category
from backend.serializers import CategorySerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


class CategoryListAPIViwes(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        categories = Category.objects.all()
        categoryserializer = CategorySerializer(categories, many = True)
        return Response(
            categoryserializer.data,
            status=status.HTTP_200_OK
        )