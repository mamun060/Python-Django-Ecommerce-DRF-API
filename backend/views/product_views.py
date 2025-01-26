from django.http import JsonResponse
from django.shortcuts import render , get_object_or_404 , redirect
from backend.models import Category, Product , ProductGallery, Cart, CartItem, Brand

def shop(request):
    products = Product.objects.all()
    brands = Brand.objects.all()
    categories = Category.objects.all()

    # Getting selected categories and brands from the GET request
    selected_categories = request.GET.getlist('categories')
    selected_brands = request.GET.getlist('brands')

    # Filtering products based on selected categories
    if selected_categories:
        products = products.filter(category__id__in=selected_categories)

    # Filtering products based on selected brands
    if selected_brands:
        products = products.filter(brand__id__in=selected_brands)

    return render(request, 'frontend/shop.html', {
        "products": products,
        "brands": brands,
        "categories": categories,
        "selected_categories": selected_categories,
        "selected_brands": selected_brands,
    })

def product_details(request, slug):
    product = Product.objects.get(slug=slug)
    product_gallery = ProductGallery.objects.filter(product_id=product)
    return render(request, 'frontend/product-details.html', {
        "product": product,
        "product_gallery": product_gallery
    })
