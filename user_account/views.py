from django.shortcuts import render
from django.http import HttpResponse

def user_account(request):
  context = {
    'dashboard': 'Dashboard content goes here'
  }

  return render(request, 'user_account.html', context)
