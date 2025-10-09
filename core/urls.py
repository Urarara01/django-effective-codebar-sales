# core/urls.py

from django.urls import path
from django.shortcuts import render
from django.contrib.auth.decorators import login_required # Para proteger la vista de inicio

@login_required # La página de inicio requiere login
def home_view(request):
    return render(request, 'core/home.html')

urlpatterns = [
    path('', home_view, name='home'),
]
# Esta URL configura la vista de inicio de la aplicación. 
# La vista `home_view` renderiza una plantilla llamada `home.html`. 
# La decoración `@login_required` asegura que solo los usuarios autenticados puedan acceder a esta página.
# Si un usuario no autenticado intenta acceder, 
# será redirigido a la página de inicio de sesión definida en 
# las configuraciones de Django.