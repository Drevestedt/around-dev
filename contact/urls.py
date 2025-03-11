from django.urls import path
from . import views

urlpatterns = [
  path('contact/', views.contact_request, name='contact'),
  path('success/', views.success_conf, name='success'),
]
