from django.urls import path, include
from backend.apiViews import brand_api_views , customer_api_views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# This urls file use for only api
urlpatterns = [
    path('brands', brand_api_views.BrandListAPIView.as_view() , name="brand-lists"),
    
    # JWT authentication endpoints
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),

    # API endpoints
    path('customers/register', customer_api_views.CustomerRegistrationView.as_view(), name='customer_register'),
    path('customers/login', customer_api_views.CustomerLoginView.as_view(), name='customer_login'),
]