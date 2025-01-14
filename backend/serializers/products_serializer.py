from rest_framework import serializers
from backend.models import Product
from backend.serializers import BrandSerializer, CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'