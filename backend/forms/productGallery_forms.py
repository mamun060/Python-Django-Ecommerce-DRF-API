from django import forms
from backend.models import ProductGallery

class ProductGalleryForm(forms.ModelForm):
    class Mate:
        model = ProductGallery
        fields = ['gallery_image']