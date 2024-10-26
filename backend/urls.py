from django.urls import path, include
from backend.apiViews import brand_api_views

urlpatterns = [
    path('brands', brand_api_views.BrandListAPIView.as_view() , name="brand-lists"),
]