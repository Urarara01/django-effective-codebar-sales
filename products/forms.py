from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    # Formulario para crear o editar un producto
    class Meta: # Definimos los metadatos del formulario
        model = Product # Especificamos el modelo al que está asociado este formulario
        fields = ['name', 'description', 'stock', 'price'] # No incluimos 'barcode' aquí, se generará automáticamente
        widgets = {
            'name': forms.TextInput(attrs={'class': 'shadow appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:border-indigo-500'}),
            'description': forms.Textarea(attrs={'class': 'shadow appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:border-indigo-500', 'rows': 3}),
            'stock': forms.NumberInput(attrs={'class': 'shadow appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:border-indigo-500', 'min': '0'}),
            'price': forms.NumberInput(attrs={'class': 'shadow appearance-none border rounded-md w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline focus:border-indigo-500', 'step': '0.01', 'min': '0'}),
        }
        labels = {
            'name': 'Nombre del Producto',
            'description': 'Descripción',
            'stock': 'Stock Inicial',
            'price': 'Precio de Venta',
        }
