from django import forms
from backend.models import Customer


class CustomerRegisterForms(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control rounded-0',
            'id': 'examplePassword',
            'placeholder': 'Enter your password'
        }
    ))

    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control rounded-0',
            'id': 'examplePassword',
            'placeholder': 'Enter your password'
        }
    ))

    class Meta:
        model = Customer
        fields = ['name', 'mobile', 'email']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control rounded-0',
                'id': 'exampleName',
                'placeholder': 'Enter your name'
            }),
            'mobile': forms.TextInput(attrs={
                'class': 'form-control rounded-0',
                'id': 'exampleMobile',
                'placeholder': 'Enter your mobile number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control rounded-0',
                'id': 'exampleEmail',
                'placeholder': 'Enter your email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control rounded-0',
                'id': 'examplePassword',
                'placeholder': 'Enter your password'
            }),
        }
    

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
