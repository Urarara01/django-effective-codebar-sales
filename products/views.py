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
        exclude_id = request.GET.get('exclude_id', None)  # ID del producto a excluir (para edición)
        
        if name:
            queryset = Product.objects.filter(name__iexact=name)
            if exclude_id:
                queryset = queryset.exclude(pk=exclude_id)
            is_unique = not queryset.exists()
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

@login_required
@user_passes_test(is_owner) # Solo el dueño puede acceder a esta vista
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_update.html', {'form': form, 'product': product})

@login_required
@user_passes_test(is_owner) # Solo el dueño puede acceder a esta vista
def report_of_the_day(request):
    from django.utils import timezone
    from django.db.models import Sum, Count, Q
    from sales.models import Sale, SaleItem
    from datetime import datetime, time
    import json
    
    # Obtener la fecha y hora actual en la zona horaria configurada
    now = timezone.now()
    today = timezone.localtime(now).date()
    
    # Crear los límites del día en la zona horaria local, luego convertir a UTC
    local_tz = timezone.get_current_timezone()
    start_of_day_local = datetime.combine(today, time.min)
    end_of_day_local = datetime.combine(today, time.max)
    
    # Hacer aware en la zona horaria local y luego convertir a UTC para las consultas
    start_of_day_utc = timezone.make_aware(start_of_day_local, local_tz)
    end_of_day_utc = timezone.make_aware(end_of_day_local, local_tz)
    
    # Estadísticas de ventas del día
    sales_today = Sale.objects.filter(sale_date__range=[start_of_day_utc, end_of_day_utc])
    
    total_sales_count = sales_today.count()
    total_revenue = sales_today.aggregate(total=Sum('total_amount'))['total'] or 0
    
    # Productos más vendidos del día
    top_products = (SaleItem.objects
                   .filter(sale__sale_date__range=[start_of_day_utc, end_of_day_utc])
                   .values('product__name', 'product__price')
                   .annotate(total_quantity=Sum('quantity'), total_revenue=Sum('subtotal'))
                   .order_by('-total_quantity')[:5])
    
    # Productos con bajo stock (menos de 10 unidades)
    low_stock_products = Product.objects.filter(stock__lt=10).order_by('stock')
    
    # Resumen de productos
    total_products = Product.objects.count()
    products_out_of_stock = Product.objects.filter(stock=0).count()
    
    # Ventas por hora del día (para gráfico)
    hourly_sales = []
    for hour in range(24):
        hour_start_local = datetime.combine(today, time(hour=hour))
        hour_end_local = datetime.combine(today, time(hour=hour, minute=59, second=59))
        
        # Convertir a UTC para las consultas
        hour_start_utc = timezone.make_aware(hour_start_local, local_tz)
        hour_end_utc = timezone.make_aware(hour_end_local, local_tz)
        
        hour_sales = Sale.objects.filter(sale_date__range=[hour_start_utc, hour_end_utc]).count()
        hourly_sales.append({'hour': f"{hour:02d}:00", 'sales': hour_sales})
    
    context = {
        'today': today,
        'total_sales_count': total_sales_count,
        'total_revenue': total_revenue,
        'top_products': top_products,
        'low_stock_products': low_stock_products,
        'total_products': total_products,
        'products_out_of_stock': products_out_of_stock,
        'hourly_sales': json.dumps(hourly_sales),  # Convertir a JSON para JavaScript
        'recent_sales': sales_today.order_by('-sale_date')[:10],  # Últimas 10 ventas
    }
    
    return render(request, 'products/report_of_the_day.html', context)