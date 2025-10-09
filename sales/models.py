from django.db import models
from products.models import Product # Importa el modelo Product
from django.contrib.auth.models import User # Importa el modelo User para registrar quién realizó la venta


# Create your models here.
class Sale(models.Model):
    sale_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Venta")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Monto Total")
    # Añadimos un campo para el usuario que realizó la venta
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Vendedor")

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        ordering = ['-sale_date'] # Ordenar por fecha de venta descendente

    def __str__(self):
        return f"Venta #{self.id} - {self.sale_date.strftime('%Y-%m-%d %H:%M')} por {self.user.username if self.user else 'Desconocido'}"

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items', verbose_name="Venta")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Producto")
    quantity = models.IntegerField(default=1, verbose_name="Cantidad")
    price_at_sale = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio al Vender")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Subtotal")

    class Meta:
        verbose_name = "Artículo de Venta"
        verbose_name_plural = "Artículos de Venta"
        # Asegura que no se dupliquen productos en la misma venta (opcional)
        unique_together = ('sale', 'product')

    def __str__(self):
        return f"{self.quantity} x {self.product.name} en Venta #{self.sale.id}"