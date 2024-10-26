### The best folder structure for Django app

```python
my_project/
│
├── my_project/                # Main project directory
│   ├── __init__.py
│   ├── settings.py            # Project-wide settings
│   ├── urls.py                # Root URLs for the entire project
│   ├── asgi.py
│   ├── wsgi.py
│   ├── static/                # Global static files (if used)
│   └── templates/             # Global templates (if used)
│
├── app_name/                  # Your app (replace 'app_name' with the actual name)
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py        # Imports for all model files
│   │   ├── user.py            # Separate model file for users
│   │   ├── product.py         # Separate model file for products
│   │   └── order.py           # Separate model file for orders
│   │
│   ├── views/
│   │   ├── __init__.py        # Imports for all view files
│   │   ├── user_views.py      # User-related views
│   │   ├── product_views.py   # Product-related views
│   │   └── order_views.py     # Order-related views
│   │
│   ├── urls.py                # URLs specific to this app
│   ├── admin.py               # Custom admin configuration
│   ├── apps.py                # App-specific settings
│   ├── forms.py               # Forms for the app
│   ├── serializers.py         # Serializers (for API, if using DRF)
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_models.py     # Tests for models
│   │   ├── test_views.py      # Tests for views
│   │   └── test_forms.py      # Tests for forms
│   │
│   ├── static/                # Static files for the app (CSS, JS, images)
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   │
│   ├── templates/
│   │   └── app_name/          # App-specific templates
│   │       ├── base.html      # App base template
│   │       ├── user.html      # User-related templates
│   │       ├── product.html   # Product-related templates
│   │       └── order.html     # Order-related templates
│   │
│   └── migrations/            # Database migrations for the app
│       ├── __init__.py
│       └── 0001_initial.py    # Example migration
│
├── manage.py
└── requirements.txt           # Project dependencies
```

### Static - for load asset file
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# media file load 
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
```

### In Django ImageField requires the pillow library
``` python
python -m pip install Pillow
```


### If you need some extra css or js file load for page wise different css and js file 
```python
{% block extra_js %} {% endblock %}
```
### Django admin Dashboard manage like list_display, filter, pagination, search
```python
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
```

### Customer login and registration and auth setup with decorations
```python
# Decoration for protect route 
from django.shortcuts import redirect
from functools import wraps

def customer_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if 'customer_id' in request.session:
            return view_func(request, *args, **kwargs)
        return redirect('customer-login')  # Redirect to login if not authenticated
    return _wrapped_view


#Customer Login functionality
def customer_login(request):
    if request.method == 'POST':
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                customer = Customer.objects.get(email=email)
                if check_password(password, customer.password):  # Check the hashed password
                    request.session['customer_id'] = customer.id  # Set session
                    return redirect('customer-dashboard')  # Redirect to home or desired page
                else:
                    messages.error(request, 'Invalid email or password.')
            except Customer.DoesNotExist:
                messages.error(request, 'Invalid email or password.')
    else:
        form = CustomerLoginForm()

    return render(request, 'frontend/account/login.html', {
        "form": form
    })

#Customer Logout Feature
def customer_logout(request):
    request.session.flush()  # Clear the session
    return redirect('customer-login')

#Customer Register
def customer_register(request):
    form = CustomerRegisterForms()  # Initialize the form
    if request.method == 'POST':
        form = CustomerRegisterForms(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.password = make_password(form.cleaned_data['password'])  # Hash the password
            customer.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('customer-login')
        else:
            messages.error(request, 'Please correct the errors below.')

    return render(request, 'frontend/account/register.html', {
        "form": form
    })
```

### Register and Login form and best approach to include custom css to the form widget 
```python
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
# register form 
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
```

### Django DRF installation for API 
### pip install djangorestframework
```python
#installted appas in settings files
INSTALLED_APPS = [
    'rest_framework',
]
```
### Model Seriliazer
```python
from rest_framework import serializers
from backend.models import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
```

### Write View for api create 
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.models import Brand
from backend.serializers import BrandSerializer

class BrandListAPIView(APIView):
    def get(self, request):
            brands = Brand.objects.all()
            serializerBrand = BrandSerializer(brands, many = True)
            return Response(
                serializerBrand.data,
                status=status.HTTP_200_OK
            )
```

### API url 
```python
from django.urls import path, include
from backend.apiViews import brand_api_views

urlpatterns = [
    path('brands', brand_api_views.BrandListAPIView.as_view() , name="brand-lists"),
]
```