from django.urls import path, include
from backend.views import frontend_views, product_views, blog_views, account_views, cart_views


# This urls file use for only api
urlpatterns = [
     # frontend url 
    path('', frontend_views.home , name='home'),
    path('shop', product_views.shop, name="shop"),
    path('shop/<slug:slug>', product_views.product_details, name="product-details"),
    path('about-us', frontend_views.about_us, name="about-us"),
    path('contact-us',frontend_views.contact, name="contact-us"),
    path('blogs', blog_views.blogs, name="blogs"),
    path('blog/<slug:slug>', blog_views.blog_details, name="blog-details"),
    path('wishlist', frontend_views.wishlist, name="wishlist"),

    #customer account route 
    path('user/dashboard', account_views.customer_dashboard, name="customer-dashboard"),
    path('user/login', account_views.customer_login, name="customer-login"),
    path('user/register', account_views.customer_register, name="customer-register"),
    path('user/profile', account_views.customer_profile, name="customer-profile"),
    path('user/logout', account_views.customer_logout , name="customer-logout"),
    path('checkout', account_views.checkout, name="checkout"),

    # cart 
    path('cart', cart_views.cart_detail, name='cart'),
    path('cart/add/<int:product_id>', cart_views.add_to_cart, name='add_to_cart'),
    path('cart/update/<int:product_id>', cart_views.update_cart, name='update_cart'),
    path('cart/remove/<int:product_id>', cart_views.remove_from_cart, name='remove_from_cart'),

]