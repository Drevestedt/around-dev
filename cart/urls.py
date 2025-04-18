from django.urls import path
from . import views

urlpatterns = [
  path('', views.cart, name='cart'),
  path('remove/<int:service_id>/', views.remove_from_cart, name='remove_from_cart'),
]
