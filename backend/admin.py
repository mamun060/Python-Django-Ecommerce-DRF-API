from django.contrib import admin
from .models import Category, Customer, Profile, Review, Product, Order, OrderItem, Author, Blog, Comment

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "description" , "category_thumbnail" , "created_at")
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
