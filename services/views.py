from django.shortcuts import render, redirect, get_object_or_404
from .forms import SelectService
from .models import Service, Cart

def add_to_cart(request):
  if request.method == 'post':
    form = SelectService(request.POST)
    if form.is_valid():
      # Get the selected service IDs  
      selected_service_ids = form.cleaned_data['please_choose_one_or_more_services']

      # Retrieve the selected services from the database
      selected_services = Service.objects.filter(id__in=selected_service_ids)

      # Create a new cart or get the existing one for the user
      if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)

      # Add the selected services to the cart
      for service in selected_services:
        cart.services.add(service)

  else:
    form = SelectService()

  return render(request, 'services.html', {'form':form})
