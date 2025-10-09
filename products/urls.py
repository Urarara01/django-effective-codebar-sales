# products/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('new/', views.product_create, name='product_create'), # Nueva URL para crear producto
    path('check_name/', views.check_product_name_unique, name='check_product_name_unique'), # Nueva URL para validar nombre
    path('<int:pk>/', views.product_detail, name='product_detail'),
]
# Este archivo define las URLs específicas de la aplicación de productos.
# - La URL raíz ('') muestra la lista de productos.