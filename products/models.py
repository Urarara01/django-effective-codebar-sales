from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre") # Verbose_name es el nombre legible para el usuario
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.IntegerField(default=0, verbose_name="Stock")
    # El campo barcode ahora es obligatorio y único
    barcode = models.CharField(max_length=100, unique=True, verbose_name="Código de Barras")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta: # Definimos los metadatos del modelo
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['name']

    def __str__(self):
        return self.name