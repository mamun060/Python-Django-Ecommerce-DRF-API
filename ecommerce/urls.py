from django.contrib import admin
from django.urls import path , include
from backend.views import frontend_views

urlpatterns = [
    path('', frontend_views.home , name='home'),
    path('product-details/', frontend_views.product_details, name="product-details"),
    path('about-us/', frontend_views.about_us, name="about-us"),
    path('contact-us',frontend_views.contact, name="contact-us"),
    path('admin/', admin.site.urls),
]
