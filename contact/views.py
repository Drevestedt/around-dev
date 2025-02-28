from django.shortcuts import render, redirect
from .forms import ContactRequestForm 

def contact_request(request):
  if request.method == "POST":
    form = ContactRequestForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("success_page")
  else:
    form = ContactRequestForm()

  return render(request, "contact_form.html", {"form": form})
