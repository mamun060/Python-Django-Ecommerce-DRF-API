from django.contrib import admin
from .models import Category, Customer, Profile, Review, Product, Order, OrderItem, Author, Blog, Comment , ProductGallery
from django.utils.html import format_html

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "description" , "category_thumbnail" )
admin.site.register(Category, categoryAdmin)

admin.site.register(Customer)
admin.site.register(Profile)
admin.site.register(Review)

#Product gallery images 
class ProductGalleryInline(admin.TabularInline): # or admin.StackedInline
    model = ProductGallery
    extra = 1
    fields = ['gallery_image', 'image_preview']
    readonly_fields = ['image_preview']
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
        return "No Image"

    image_preview.short_description = 'Preview'

# product model
class productAdmin(admin.ModelAdmin):
    inlines = [ProductGalleryInline]
    list_display = (
        "product_title",
        "slug", 
        "sub_title", 
        "product_description", 
        "price", 
        "color",
        "size", 
        "product_thumbnail",
        )
admin.site.register(Product, productAdmin)
# end product model

# Product Gallery Admin 
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ('product', 'gallery_image', 'created_at')
    search_fields = ('product__product_title',)
admin.site.register(ProductGallery, ProductGalleryAdmin)


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
