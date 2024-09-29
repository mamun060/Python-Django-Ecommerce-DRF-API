from django import forms
from backend.models import Customer

class CustomerLoginForm(forms.Form):
    email = forms.EmailField( 
        widget=forms.TextInput(attrs={
            'class': 'form-control rounded-0',
            'id': 'exampleUsername',
            'placeholder': 'Enter your username'
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control rounded-0',
            'id': 'examplePassword',
            'placeholder': 'Enter your password'
        })
    )


