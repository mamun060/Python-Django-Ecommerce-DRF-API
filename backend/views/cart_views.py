from django.http import JsonResponse , HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import get_object_or_404 , render ,redirect
from backend.models import Product , Cart , CartItem , Customer 
from backend.decorators import customer_required

@customer_required
def add_to_cart(request, product_id):
    if request.method == "POST":
        customer_id = request.session.get('customer_id')
        
        # Check if the customer exists
        if not customer_id:
            return JsonResponse({"error": "Customer not logged in"}, status=403)

        # Get the product by ID
        product = get_object_or_404(Product, id=product_id)

        # Get or create a cart for the customer
        cart, created = Cart.objects.get_or_create(customer_id=customer_id)

        # Get or create a CartItem for the product in the cart
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        if created:
            cart_item.quantity = 1  # If it's new, set quantity to 1
        else:
            cart_item.quantity += 1  # If it exists, increment the quantity

        cart_item.save()  # Save the cart item

        return JsonResponse({
            "message": "Product added to cart!",
            "quantity": cart_item.quantity
        }, status=200)
    
    return JsonResponse({"error": "Invalid request"}, status=400)


def cart_detail(request):
    customer_id = request.session.get('customer_id')
    customer = get_object_or_404(Customer, id=customer_id)
    cart = get_object_or_404(Cart, customer=customer)

    # Retrieve all cart items
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'frontend/cart-details.html',{
        "cart_items": cart_items,
        "total_price": total_price
    })


def update_cart(request, product_id):
    if request.method == "POST" and request.is_ajax():
        customer = get_object_or_404(Customer, user=request.user)
        cart = get_object_or_404(Cart, customer=customer)
        cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)

        quantity = int(request.POST.get("quantity", 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
            return JsonResponse({"message": "Cart updated", "quantity": cart_item.quantity}, status=200)
        else:
            cart_item.delete()
            return JsonResponse({"message": "Item removed from cart"}, status=200)

    return JsonResponse({"error": "Invalid request"}, status=400)




def remove_from_cart(request, product_id):
    if request.method == "POST" and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Get the customer from the session using the stored customer_id
        customer_id = request.session.get('customer_id')
        customer = get_object_or_404(Customer, id=customer_id)
        
        # Get the cart associated with the customer
        cart = get_object_or_404(Cart, customer=customer)
        
        # Get the cart item to be removed
        cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
        cart_item.delete()

        return JsonResponse({"message": "Item removed from cart"}, status=200)

    return JsonResponse({"error": "Invalid request"}, status=400)