from django.shortcuts import render , get_object_or_404 , redirect
from backend.models import Customer
from backend.forms import CustomerLoginForm, CustomerRegisterForms
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from backend.decorators import customer_required

# customer account page
@customer_required
def customer_dashboard(request):
    return render(request, 'frontend/account/dashboard.html')

# Customer Login view 
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

#Customer Logout view
def customer_logout(request):
    request.session.flush()  # Clear the session
    return redirect('customer-login')

# customer register view 
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

@customer_required
# Customer Profile view
def customer_profile(request):
    return render(request, 'frontend/account/profile.html')

@customer_required
def checkout(request):
    return render(request, 'frontend/checkout.html')