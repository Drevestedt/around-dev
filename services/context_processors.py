from .models import Cart

def cart_item_count(request):
  count = 0
  try:
    if request.user.is_authenticated:
      cart = Cart.objects.filter(user=request.user).first()
    else:
      cart = Cart.objects.filter(user=None).first()
    if cart:
      count = cart.services.count()
  except:
    count = 0;
  return {'cart_item_count': count}

def cart_item_price(request):
  min_price = 0 
  try:
    if request.user.is_authenticated:
      cart = Cart.objects.filter(user=request.user).first()
    else:
      cart = Cart.objects.filter(user=None).first()
    if cart:
      min_price = min(service.price for service in cart.services.all())
  except:
    pass
  return {'cart_item_price': min_price}
