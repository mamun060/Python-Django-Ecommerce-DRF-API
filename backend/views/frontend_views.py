from django.shortcuts import render , get_object_or_404 , redirect
from backend.models import  Category, Product , ProductGallery, Brand
from backend.forms import CommentForm

#Here is include frontend views
def home(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    return render(request, 'frontend/home.html',{
        "categories": categories,
        "brands": brands
    })

def about_us(request):
    return render(request , 'frontend/about.html')

def contact(request):
    return render(request, 'frontend/contact.html')

def wishlist(request):
    return render(request, 'frontend/wishlist.html')

