from django.shortcuts import render

#Here is include frontend views
def home(request):
    return render(request, 'frontend/home.html')

def product_details(request):
    return render(request, 'frontend/product-details.html')

def about_us(request):
    return render(request , 'frontend/about.html')

def contact(request):
    return render(request, 'frontend/contact.html')