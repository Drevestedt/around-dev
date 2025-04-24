from django.shortcuts import render, redirect
from django.http import HttpResponse

def user_account(request):
  services = request.session.get('services', [])
  context = {
    'services': services
  }
  return render(request, 'user_account.html', context)


def add_services_to_account(request):
  if request.method == 'POST':
    service = request.POST.get('service')
    rate = request.POST.get('rate')

    if 'services' not in request.session: #TODO: Change to store in a model instead of session
      request.session['services'] = []

    request.session['services'].append({'service': service, 'rate': rate})
    request.session.modified = True

  return redirect('user_account')