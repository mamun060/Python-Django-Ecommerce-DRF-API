from django import forms
from backend.models import Product

class ProductForms(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['file']
        widgets = {
            'file': forms.FileInput(attrs={'multiple': True})
        }