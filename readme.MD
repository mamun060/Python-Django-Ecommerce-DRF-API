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
```
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
