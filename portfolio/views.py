from django.shortcuts import render
from .models import Project
from django.conf import settings
from django.views.static import serve

def portfolio(request):
  projects = Project.objects.all()

  return render(request, "portfolio.html", {'projects': projects})


# To serve media files manually
def media_serve(request, path):
    return serve(request, path, document_root=settings.MEDIA_ROOT)
