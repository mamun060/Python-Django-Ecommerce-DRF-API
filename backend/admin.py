from django.contrib import admin
from .models import Category, Customer, Profile, Review, Product, Order, OrderItem, Author, Blog, Comment
from backend.forms import ProductForms

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "description" , "thumbnail" , "created_at")
admin.site.register(Category, categoryAdmin)

admin.site.register(Customer)
admin.site.register(Profile)
admin.site.register(Review)

# product model
class productAdmin(admin.ModelAdmin):
    form = ProductForms
    def save_model(self, request, obj, form, change):
        # If multiple files are uploaded, handle each file
        files = request.FILES.getlist('file')
        for file in files:
            Product.objects.create(file=file)

    list_display = (
        "product_title", 
        "sub_title", 
        "product_description", 
        "price", 
        "color",
        "size", 
        "product_thumbnail",
        "product_gallery",

        )
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'category', 'price', 'discount_price')
    fields = ['category', 'product_title', 'sub_title', 'product_description', 'price', 
              'discount_price', 'color', 'size', 'product_thumbnail', 'product_gallery']
admin.site.register(Product, productAdmin)
# end product model

admin.site.register(Order)
admin.site.register(OrderItem)

class authorAdmin(admin.ModelAdmin):
    list_display = ("name","email","phone")
admin.site.register(Author, authorAdmin)

class blogAdmin(admin.ModelAdmin):
    list_display = ("author_id","title", "sub_title" , "description" , "thumbnail")
admin.site.register(Blog, blogAdmin)

class commentAdmin(admin.ModelAdmin):
    list_display = ("get_post_title" , "name" , "email" , "comment")
    list_filter = ('post_id',)  # Add filtering by post
    search_fields = ('name', 'email', 'comment')  # Enable search
    list_per_page = 10

    # Define a method to display the post title
    def get_post_title(self, obj):
        return obj.post.title 
    
    # Set the display name for the column
    get_post_title.short_description = 'Post Title'
admin.site.register(Comment, commentAdmin)
