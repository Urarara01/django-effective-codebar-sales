# sales/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.create_sale_view, name='create_sale'),
    path('add_product/', views.add_product_to_sale_api, name='add_product_to_sale_api'),
    path('complete_sale/', views.complete_sale_api, name='complete_sale_api'), # Nueva URL para completar la venta
]