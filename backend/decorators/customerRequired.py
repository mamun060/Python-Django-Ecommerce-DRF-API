from django.shortcuts import redirect
from functools import wraps

def customer_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if 'customer_id' in request.session:
            return view_func(request, *args, **kwargs)
        return redirect('customer-login')  # Redirect to login if not authenticated
    return _wrapped_view
