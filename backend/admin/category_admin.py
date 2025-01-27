from django.contrib import admin
from backend.models import Category

class categoryAdmin(admin.ModelAdmin):
    list_display = ("category_name", "description" , "category_thumbnail" )
admin.site.register(Category, categoryAdmin)
