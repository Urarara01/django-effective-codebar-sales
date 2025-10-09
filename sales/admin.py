from django.contrib import admin
from .models import Sale, SaleItem
from products.models import Product # Importa Product para actualizar stock
from django.db.models import F # Para operaciones atómicas de base de datos


# Register your models here.
class SaleItemInline(admin.TabularInline): # Permite editar SaleItems directamente en la página de Sale
    model = SaleItem
    extra = 0 # No mostrar campos vacíos por defecto
    fields = ('product', 'quantity', 'price_at_sale', 'subtotal')
    readonly_fields = ('price_at_sale', 'subtotal') # Estos se calcularán automáticamente

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale_date', 'total_amount', 'user')
    list_filter = ('sale_date', 'user')
    inlines = [SaleItemInline]
    readonly_fields = ('total_amount',) # El total se calculará automáticamente

    # Sobreescribir save_model para manejar la lógica de stock cuando se guarda desde el admin
    def save_model(self, request, obj, form, change):
        is_new_sale = not change # Si no es un cambio, es una nueva venta
        super().save_model(request, obj, form, change) # Guarda la venta primero

        if is_new_sale:
            # Si es una nueva venta, asigna el usuario actual
            obj.user = request.user
            obj.save() # Guarda la venta de nuevo para asignar el usuario

        # Recalcular el total y actualizar stock para todos los items de la venta
        total = 0
        for item in obj.items.all():
            # Si el item es nuevo o la cantidad ha cambiado
            if item.pk is None or 'quantity' in item._changed_fields or 'product' in item._changed_fields:
                # Asegurarse de que el precio al vender y subtotal estén correctos
                item.price_at_sale = item.product.price
                item.subtotal = item.quantity * item.price_at_sale
                item.save()

                # Actualizar stock (solo si es una nueva venta o si el item se añadió/modificó)
                if is_new_sale or item.pk is None: # Si es una nueva venta o un nuevo item en una venta existente
                    Product.objects.filter(id=item.product.id).update(stock=F('stock') - item.quantity)
                # Si es un cambio en un item existente, la lógica de stock sería más compleja
                # para manejar aumentos/disminuciones, pero para una primera versión,
                # nos enfocamos en la creación de la venta.

            total += item.subtotal
        
        obj.total_amount = total
        obj.save() # Guarda el total actualizado

