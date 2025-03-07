from django.shortcuts import render
from portfolio.models import Project

def base(request):
  return render(request, 'base.html')

def home(request):
  # Display 3 projects on home page 
  # projects = Project.objects.all()[3]
  return render(request, 'home.html', {})
