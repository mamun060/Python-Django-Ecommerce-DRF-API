from django.contrib import admin
from backend.models import Product , ProductGallery
from django.utils.html import format_html

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