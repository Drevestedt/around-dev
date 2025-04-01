from django.conf import settings

def cart_content(request):
  cart_items = []
  total = 0
  service_count = 0
  
  context = {
    'cart_items': cart_items,
    'total': total,
    'service_count': service_count,
  }

  return context

