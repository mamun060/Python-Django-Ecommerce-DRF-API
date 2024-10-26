from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.models import Brand
from backend.serializers import BrandSerializer

class BrandListAPIView(APIView):
    def get(self, request):
            brands = Brand.objects.all()
            serializerBrand = BrandSerializer(brands, many = True)
            return Response(
                serializerBrand.data,
                status=status.HTTP_200_OK
            )