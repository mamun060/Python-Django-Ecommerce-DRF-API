from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.models import Brand
from backend.serializers import BrandSerializer

# Authorization permission assigned 
from rest_framework.permissions import AllowAny, IsAuthenticated

class BrandListAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
            brands = Brand.objects.all()
            serializerBrand = BrandSerializer(brands, many = True)
            return Response(
                serializerBrand.data,
                status=status.HTTP_200_OK
            )


class BrandCreateApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = BrandSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Brand created successfully",
                    "brand": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)