# products/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.utils.text import slugify
import uuid # Para generar IDs únicos
import json

from .models import Product
from .forms import ProductForm

# Función para verificar si el usuario es superusuario (dueño)
def is_owner(user):
    return user.is_superuser

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required
@user_passes_test(is_owner) # Solo el dueño puede acceder a esta vista
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False) # No guardar aún en la base de datos
            # Generar el código de barras automáticamente (Code128 compatible)
            # Usamos slugify para limpiar el nombre y uuid para asegurar unicidad
            base_barcode = slugify(product.name)[:50] # Limita la longitud para evitar códigos muy largos
            unique_id = str(uuid.uuid4()).split('-')[0] # Usa una parte de un UUID. UUID: 32 caracteres, tomamos los primeros 8 para el código de barras
            product.barcode = f"PROD-{base_barcode}-{unique_id}".upper() # Prefijo PROD- y mayúsculas

            product.save() # Guardar el producto en la base de datos
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'products/product_create.html', {'form': form})

@login_required
@user_passes_test(is_owner) # Solo el dueño puede acceder a esta vista
def check_product_name_unique(request):
    if request.method == 'GET':
        name = request.GET.get('name', '').strip()
        if name:
            is_unique = not Product.objects.filter(name__iexact=name).exists()
            return JsonResponse({'is_unique': is_unique})
    return JsonResponse({'is_unique': False}, status=400) # Bad request if no name provided or not GET

@login_required
@user_passes_test(is_owner) # Solo el dueño puede acceder a esta vista
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'products/product_confirm_delete.html', {'product': product})