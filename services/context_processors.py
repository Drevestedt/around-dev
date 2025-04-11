from .models import Cart

def cart_item_count(request):
  if request.user.is_authenticated:
    cart = Cart.objects.filter(user=request.user).first()
  else:
    cart = Cart.objects.filter(user=None).first()
  if cart:
    count = cart.services.count()
  return {'cart_item_count': count}
