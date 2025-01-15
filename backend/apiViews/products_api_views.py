from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.serializers import ProductSerializer
from backend.models import Product
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

class ProductApiViews(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            proudcts = Product.objects.all()
            SerializerProduct = ProductSerializer(proudcts, many=True, fields=["id", "product_title", "slug" , "price", "product_thumbnail"])
            filter_backends = [DjangoFilterBackend]
            filterset_fields = ['brand', 'category']
            return Response(
                SerializerProduct.data ,
                status=status.HTTP_200_OK
            )
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


class ProductDetailsApiView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, slug):
        try:
            product = Product.objects.get(slug=slug)
            serializer = ProductSerializer(product)
            return Response({
                "data": serializer.data,
                "status": status.HTTP_200_OK
            })
        except Product.DoesNotExist:
            return Response(
                {"error": "Product Details not found!"},
                status=status.HTTP_404_NOT_FOUND
            )