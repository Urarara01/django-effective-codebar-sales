# sales/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db import transaction # Para asegurar que todas las operaciones de DB sean atómicas
from django.db.models import F # Para operaciones atómicas de base de datos
import json

from products.models import Product
from .models import Sale, SaleItem

@login_required
def create_sale_view(request):
    # Esta vista cargará la interfaz de usuario para la venta
    return render(request, 'sales/create_sale.html')

@csrf_exempt # ¡Cuidado! Usar solo para APIs internas o con validación de token
@login_required # Asegura que solo usuarios logueados puedan acceder
def add_product_to_sale_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            barcode = data.get('barcode')
            
            product = Product.objects.get(barcode=barcode)
            
            return JsonResponse({
                'success': True,
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': float(product.price),
                    'stock': product.stock
                }
            })
        except Product.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Producto no encontrado.'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    return JsonResponse({'success': False, 'message': 'Método no permitido.'}, status=405)

@csrf_exempt # ¡Cuidado! Usar solo para APIs internas o con validación de token
@login_required # Asegura que solo usuarios logueados puedan acceder
def complete_sale_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cart_items = data.get('cart', [])

            if not cart_items:
                return JsonResponse({'success': False, 'message': 'El carrito está vacío.'}, status=400)

            with transaction.atomic(): # Asegura que todas las operaciones se completen o se reviertan
                new_sale = Sale.objects.create(user=request.user) # Asigna el usuario actual a la venta
                total_amount = 0

                for item_data in cart_items:
                    product_id = item_data.get('id')
                    quantity = item_data.get('quantity')
                    
                    # Linea agregada
                    user = request.user

                    product = Product.objects.select_for_update().get(id=product_id) # Bloquea el producto para evitar condiciones de carrera

                    if product.stock < quantity:
                        # Si no hay suficiente stock, revertir la transacción
                        raise ValueError(f"Stock insuficiente para {product.name}. Disponible: {product.stock}, Solicitado: {quantity}")

                    price_at_sale = product.price
                    subtotal = price_at_sale * quantity
                    total_amount += subtotal

                    SaleItem.objects.create(
                        sale=new_sale,
                        product=product,
                        quantity=quantity,
                        price_at_sale=price_at_sale,
                        subtotal=subtotal
                        
                    )
                    
                    # Decrementar el stock del producto
                    product.stock = F('stock') - quantity
                    product.save()
                    product.refresh_from_db() # Recarga el objeto para obtener el stock actualizado

                new_sale.total_amount = total_amount
                new_sale.save()

            return JsonResponse({'success': True, 'message': 'Venta completada con éxito!', 'sale_id': new_sale.id})

        except Product.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Uno de los productos no fue encontrado.'}, status=404)
        except ValueError as ve:
            return JsonResponse({'success': False, 'message': str(ve)}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': f"Error al procesar la venta: {str(e)}"}, status=500)
    return JsonResponse({'success': False, 'message': 'Método no permitido.'}, status=405)