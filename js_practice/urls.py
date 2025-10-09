from django.urls import path
from . import views

urlpatterns = [
    path('', views.playground, name='js_playground'),
    path('api/', views.api, name='js_api'),
]
