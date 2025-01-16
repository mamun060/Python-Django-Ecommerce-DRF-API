from django.urls import path, include
from backend.apiViews import (
    brand_api_views , 
    customer_api_views, 
    category_api_views, 
    products_api_views, 
    blog_api_views
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# This urls file use for only api
urlpatterns = [
    path('brands', brand_api_views.BrandListAPIView.as_view() , name="api-brand-lists"), 
    path('brand/create', brand_api_views.BrandCreateApiView.as_view() , name="api-brand-lists"), 
    path('categories', category_api_views.CategoryListAPIViwes.as_view(), name='api-category-lists'),
    path('product', products_api_views.ProductApiViews.as_view(), name="api-product-lists"),
    path('product/<slug:slug>', products_api_views.ProductDetailsApiView.as_view(), name="api-product-details"),
    path('blog', blog_api_views.BlogApiViews.as_view(), name="api-blog-lists"),
    path('blog/<slug:slug>', blog_api_views.SingleBlogApiView.as_view(), name="api-blog-details"),
    
    # JWT authentication endpoints
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),

    # API endpoints
    path('customers/register', customer_api_views.CustomerRegistrationView.as_view(), name='customer_register'),
    path('customers/login', customer_api_views.CustomerLoginView.as_view(), name='customer_login'),
]