from django.shortcuts import render

#Here is include frontend views
def home(request):
    return render(request, 'frontend/home.html')

def shop(request):
    return render(request, 'frontend/shop.html')

def product_details(request):
    return render(request, 'frontend/product-details.html')

def about_us(request):
    return render(request , 'frontend/about.html')

def contact(request):
    return render(request, 'frontend/contact.html')

def blogs(request):
    return render(request, 'frontend/blogs.html')

def blog_details(request):
    return render(request, 'frontend/blog-details.html')

def cart(request):
    return render(request, 'frontend/cart.html')

def wishlist(request):
    return render(request, 'frontend/wishlist.html')

# customer account page
def customer_dashboard(request):
    return render(request, 'frontend/account/dashboard.html')