from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json

def playground(request):
    return render(request, 'js_practice/playground.html')

@csrf_exempt  # Solo para pruebas, en producción usa CSRF correctamente
def api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre', '')
            edad = data.get('edad', '')
            return JsonResponse({
                'mensaje': f'Hola {nombre}, tienes {edad} años.',
                'recibido': data
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Solo POST permitido'}, status=405)
