from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from backend.views import frontend_views

urlpatterns = [
    # frontend url 
    path('', frontend_views.home , name='home'),
    path('shop', frontend_views.shop, name="shop"),
    path('product-details', frontend_views.product_details, name="product-details"),
    path('about-us', frontend_views.about_us, name="about-us"),
    path('contact-us',frontend_views.contact, name="contact-us"),
    path('blogs', frontend_views.blogs, name="blogs"),
    path('blog/<slug:slug>', frontend_views.blog_details, name="blog-details"),
    path('cart', frontend_views.cart, name="cart"),
    path('wishlist', frontend_views.wishlist, name="wishlist"),

    #customer account route 
    path('customer-dashboard', frontend_views.customer_dashboard, name="customer-dashboard"),
    # Django super admin url
    path('admin/', admin.site.urls),
]

# media file access
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)