from django.http import JsonResponse , HttpResponseForbidden
from django.shortcuts import get_object_or_404 , render ,redirect
from backend.models import Product , Cart , CartItem , Customer 


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('shop')


def cart_detail(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "You need to be logged in to view the cart."}, status=403)

    customer = get_object_or_404(Customer, user=request.user)
    cart = get_object_or_404(Cart, customer=customer)

    return render(request, 'frontend/account/cart-details.html', {'cart': cart})


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
    if request.method == "POST" and request.is_ajax():
        customer = get_object_or_404(Customer, user=request.user)
        cart = get_object_or_404(Cart, customer=customer)
        cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
        cart_item.delete()

        return JsonResponse({"message": "Item removed from cart"}, status=200)

    return JsonResponse({"error": "Invalid request"}, status=400)
