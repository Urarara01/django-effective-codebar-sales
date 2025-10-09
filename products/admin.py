from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'barcode', 'created_at')
    search_fields = ('name', 'barcode')
    list_filter = ('created_at',)
    # Hacer el campo barcode de solo lectura si lo generas automáticamente
    readonly_fields = ('barcode',)