from django.shortcuts import render, redirect
from services.models import Cart
from django.views.decorators.http import require_POST

def cart(request):
    # Retrieve the cart for the logged-in user or an anonymous user
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        cart = Cart.objects.filter(user=None).first()
    
    # Check if the cart exists
    services = cart.services.all() if cart else []

    return render(request, 'cart.html', {'cart_items': services})

def remove_from_cart(request, service_id):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        cart = Cart.objects.filter(user=None).first()
    
    if cart:
        cart.services.remove(service_id)

    return redirect('cart')
