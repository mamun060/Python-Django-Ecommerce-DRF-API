from django.contrib import admin
from backend.models import Brand

class brandAdmin(admin.ModelAdmin):
    list_display = ("name" , "description" , "thumbnail")
admin.site.register(Brand, brandAdmin)