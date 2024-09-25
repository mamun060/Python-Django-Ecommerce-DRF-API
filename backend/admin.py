from django.contrib import admin
from .models import Category, Customer, Profile, Review, Product, Order, OrderItem, Author, Blog, Comment

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "description" , "category_thumbnail")
admin.site.register(Category, categoryAdmin)

admin.site.register(Customer)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)

class authorAdmin(admin.ModelAdmin):
    list_display = ("name","email","phone")
admin.site.register(Author, authorAdmin)

class blogAdmin(admin.ModelAdmin):
    list_display = ("author_id","title", "sub_title" , "description" , "thumbnail")
admin.site.register(Blog, blogAdmin)

admin.site.register(Comment)
