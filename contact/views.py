from django.shortcuts import render
from .models import contactRequest

def contact_request(request):
  return render(request, "contact_form.html", {})
