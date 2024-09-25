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

### Dynamic url path
```python
