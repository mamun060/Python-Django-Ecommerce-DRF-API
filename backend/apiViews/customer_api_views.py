from rest_framework import generics, status
from rest_framework.response import Response
from backend.models import Customer
from backend.serializers import CustomerSerializer  # Ensure you have a serializer for the Customer model
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

class CustomerRegistrationView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [AllowAny]  # Allow any user to access this endpoint

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Hash the password before saving
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomerLoginView(APIView):
    permission_classes = [AllowAny]  # Allow any user to access this endpoint

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            customer = Customer.objects.get(email=email)
            if check_password(password, customer.password):  # Check the hashed password
                # Create JWT token
                refresh = RefreshToken.for_user(customer)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'customer_id': customer.id
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except Customer.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)