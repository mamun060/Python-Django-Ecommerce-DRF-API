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

### Django Rest Framework JWT token based authentication and Authorization practice.

### install jwt package 
pip install djangorestframework-simplejwt

### Configure Django Settings for JWT Authentication
```python
# Add 'rest_framework' and 'rest_framework_simplejwt' to your INSTALLED_APPS
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
]

# Configure REST framework with JWT authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',  # Requires authentication by default
    ),
}

# JWT Configuration (Optional)
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),  # Token expires after 15 minutes
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),     # Refresh token valid for 7 days
    'ROTATE_REFRESH_TOKENS': True,                   # Issue new refresh token on use
    'BLACKLIST_AFTER_ROTATION': True,                # Blacklist old tokens after rotation
}
```
### DRF Views
```python
# Django REST Framework Views Series:

# APIViews - Mainly class based view
from rest_framework.response import Response
from rest_framework.views import APIView

class DeleteAllItems(APIView):
    def get(self, request):
        #body - other operations
    
# api_view() - mainly function based view 
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view(['DELETE'])
def get(request):
    # function body
```
### DRF Viewset
```python
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from myapps.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response

# viewset example
class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

# Viewset action lists
class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        pass
    def create(self, request):
        pass
    def retrieve(self, request, pk=None):
        pass
    def update(self, request, pk=None):
        pass
    def partial_update(self, request, pk=None):
        pass
    def destroy(self, request, pk=None):
        pass

#If we need to, we can bind this viewset into two separate views, like so:
user_list = UserViewSet.as_view({'get': 'list'})
user_detail = UserViewSet.as_view({'get': 'retrieve'})
```
### DRF permission wise api access
```python
# first setting DRF permission
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}

# class based view permission 
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        content = model.objects.all()
        return Response(content)

# function based view permission 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = model.objects.all()
    return Response(content)
```

### Create URLs for JWT Authentication
```python
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    # JWT authentication endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
# /api/token/: Obtain access and refresh tokens.
# /api/token/refresh/: Use the refresh token to get a new access token.
# /api/token/verify/: Verify if a token is valid.
```

### Protect API Endpoints with JWT Authentication
```python
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models.brand import Brand
from .serializers import BrandSerializer

class BrandListAPIView(APIView):
    permission_classes = [IsAuthenticated]  # Requires JWT authentication

    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)
```

### Public Access API Endpoints without JWT Authentication
```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.models import Brand
from backend.serializers import BrandSerializer
# Authorization permission assigned 
from rest_framework.permissions import AllowAny

class ProductApiViews(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            proudcts = Product.objects.all()
            SerializerProduct = ProductSerializer(proudcts, many=True)
            return Response(
                SerializerProduct.data ,
                status=status.HTTP_200_OK
            )
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

# single product details API endpoint
class ProductDetailsApiView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, slug):
        try:
            product = Product.objects.get(slug=slug)
            serializer = ProductSerializer(product)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        except Product.DoesNotExist:
            return Response(
                {"error": "Product Details not found!"},
                status=status.HTTP_404_NOT_FOUND
            )
```

### Django DRF defualt filter library
```python
install: pip install django-filter
# first - setup settings file 
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

# second step - setup serializer where you need to apply filter
from rest_framework import serializers
from backend.models import Product
from backend.serializers import BrandSerializer, CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'

# 3rd step - apply api filter views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.serializers import ProductSerializer
from backend.models import Product
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

class ProductApiViews(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            proudcts = Product.objects.all()
            SerializerProduct = ProductSerializer(proudcts, many=True)
            filter_backends = [DjangoFilterBackend]
            filterset_fields = ['brand', 'category']
            return Response(
                SerializerProduct.data ,
                status=status.HTTP_200_OK
            )
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
```

### DRF - Serializer Model Relationship
```python
#01 => slug related Field
class AlbumSerializer(serializers.ModelSerializer):
    tracks = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
     )

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']

#02=> Nested relationship - example

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']

#03=> Writeable Nested Serializers
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['order', 'title', 'duration']

class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']

    def create(self, validated_data):
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album
```

### Django-silk = for api profiling and optimization library
```python
#install: pip install django-silk

#Settings 
MIDDLEWARE_CLASSES = (
    'silk.middleware.SilkyMiddleware',
)

INSTALLED_APPS = (
    'silk'
)

# Add the following to your urls.py:
urlpatterns = [
    path('silk/', include('silk.urls', namespace='silk')),
]

# then migrate again 
python manage.py makemigrations
python manage.py migrate
```