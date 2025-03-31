from django.conf import settings

def bag_content(request):
  bag_items = []
  total = 0
  service_count = 0
  
  context = {
    'bag_items': bag_items,
    'total': total,
    'service_count': service_count,
  }

  return context

