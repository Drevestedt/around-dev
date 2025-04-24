from django.urls import path
from . import views

urlpatterns = [
  path('', views.user_account, name='user_account'),
  path('add_services_to_account/', views.add_services_to_account, name='add_services_to_account')
]
