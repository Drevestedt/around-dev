from django.shortcuts import render
from services.models import Cart

def cart(request):
    # Retrieve the cart for the logged-in user or an anonymous user
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        cart = Cart.objects.filter(user=None).first()
    
    # Check if the cart exists
    services = cart.services.all() if cart else []

    return render(request, 'cart.html', {'cart_items': services})
