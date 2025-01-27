from django.contrib import admin
from backend.models import Author, Blog, Comment


# Author model register in admin
class authorAdmin(admin.ModelAdmin):
    list_display = ("name","email","phone")
admin.site.register(Author, authorAdmin)

# blog model register in admin
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