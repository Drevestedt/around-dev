from django.shortcuts import render
from .forms import SelectService

def services(request):
  form = SelectService()
  return render(request, 'services.html', {'form':form})
