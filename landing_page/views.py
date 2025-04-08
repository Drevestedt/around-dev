from django.shortcuts import render
from portfolio.models import Project

def base(request):
  return render(request, 'base.html')

def home(request):
  projects = Project.objects.filter(featured=True)[:3]
  return render(request, 'home.html', {'projects': projects})
