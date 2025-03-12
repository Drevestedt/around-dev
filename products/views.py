from django.shortcuts import render
from .forms import SelectService

def products(request):
  form = SelectService()
  return render(request, 'products.html', {'form':form})
