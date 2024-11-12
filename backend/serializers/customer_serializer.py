# backend/apiViews/customer_serializer.py
from rest_framework import serializers
from backend.models import Customer  # Adjust the import based on your project structure

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'mobile', 'email', 'password', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True}  # Make the password field write-only
        }

    def create(self, validated_data):
        # Hash the password before saving
        customer = Customer(
            name=validated_data['name'],
            mobile=validated_data['mobile'],
            email=validated_data['email'],
            password=validated_data['password']  # You should hash this before saving
        )
        customer.set_password(validated_data['password'])  # Hash the password
        customer.save()
        return customer

    def update(self, instance, validated_data):
        # Update the customer instance
        instance.name = validated_data.get('name', instance.name)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.email = validated_data.get('email', instance.email)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])  # Hash the password if it has changed
        instance.save()
        return instance
