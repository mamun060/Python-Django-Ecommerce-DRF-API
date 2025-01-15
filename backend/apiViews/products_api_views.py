from django.db.models import Max, Min
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from backend.serializers import ProductSerializer, ProductInfoSerializer
from backend.models import Product
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend


class ProductApiViews(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            products = Product.objects.all()
            SerializerProduct = ProductSerializer(products, many=True, fields=["id", "product_title", "slug" , "price", "product_thumbnail"])
            filter_backends = [DjangoFilterBackend]
            filterset_fields = ['brand', 'category']
            # Aggregate min and max price
            min_price = products.aggregate(min_price=Min('price'))['min_price']
            max_price = products.aggregate(max_price=Max('price'))['max_price']

            # Prepare response
            return Response({
                "products": SerializerProduct.data,
                "total_products": products.count(),
                "min_price": min_price,
                "max_price": max_price,
            })
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


class ProductInfoApiView(APIView):
    permission_classes = [AllowAny]
    def get(request):
        products = Product.objects.all()
        serializer = ProductInfoSerializer({
            'products': products,
            'count': len(products),
            'max_price': products.aggregate(max_price=Max('price'))['max_price']
        })
        return Response(serializer.data)