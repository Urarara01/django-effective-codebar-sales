# Documentación Técnica - Sistema de Automatización de Tienda con Código de Barras

## Tabla de Contenidos
1. [Información General](#información-general)
2. [Arquitectura del Sistema](#arquitectura-del-sistema)
3. [Tecnologías Utilizadas](#tecnologías-utilizadas)
4. [Estructura del Proyecto](#estructura-del-proyecto)
5. [Modelos de Datos](#modelos-de-datos)
6. [Funcionalidades Principales](#funcionalidades-principales)
7. [API Endpoints](#api-endpoints)
8. [Sistema de Autenticación](#sistema-de-autenticación)
9. [Frontend y UX](#frontend-y-ux)
10. [Configuración y Deployment](#configuración-y-deployment)
11. [Consideraciones de Seguridad](#consideraciones-de-seguridad)
12. [Guía de Instalación](#guía-de-instalación)

## Información General

### Descripción del Proyecto
Sistema web desarrollado en Django para la automatización de ventas en tiendas mediante el uso de códigos de barras. El sistema permite gestionar productos, realizar ventas mediante escáner de códigos de barras y llevar un control de inventario en tiempo real.

### Objetivos
- Automatizar el proceso de ventas utilizando códigos de barras
- Gestionar inventario de productos de forma eficiente
- Proporcionar una interfaz intuitiva para empleados y propietarios
- Mantener un registro detallado de todas las transacciones

### Alcance
El sistema cubre:
- Gestión completa de productos (CRUD)
- Sistema de ventas con escáner de códigos de barras
- Control de inventario en tiempo real
- Autenticación de usuarios con roles diferenciados
- Interfaz web responsive

## Arquitectura del Sistema

### Patrón de Arquitectura
El proyecto sigue el patrón **Model-View-Template (MVT)** de Django:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│     Template    │────│      View       │────│      Model      │
│   (Frontend)    │    │   (Lógica)      │    │  (Base de Datos)│
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Arquitectura de Apps
```
tienda_project/
├── core/           # App principal (home, navegación)
├── products/       # Gestión de productos
├── sales/          # Sistema de ventas
├── js_practice/    # Utilidades JavaScript
└── tienda_project/ # Configuración principal
```

## Tecnologías Utilizadas

### Backend
- **Django 5.2.7**: Framework web principal
- **Python 3.10+**: Lenguaje de programación
- **SQLite3**: Base de datos (desarrollo)
- **Django ORM**: Mapeo objeto-relacional

### Frontend
- **HTML5**: Estructura de páginas
- **CSS3**: Estilos personalizados
- **Tailwind CSS**: Framework de utilidades CSS
- **JavaScript (Vanilla)**: Interactividad
- **Fetch API**: Comunicación AJAX

### Herramientas de Desarrollo
- **Git**: Control de versiones
- **Django Debug Toolbar**: Depuración (desarrollo)
- **Ngrok**: Túneles seguros para testing

## Estructura del Proyecto

```
shop-automatization-with-barcode/
├── manage.py                    # Script de gestión Django
├── db.sqlite3                   # Base de datos SQLite
├── DOCUMENTACION_TECNICA.md     # Esta documentación
├── tienda_project/              # Configuración principal
│   ├── __init__.py
│   ├── settings.py              # Configuraciones globales
│   ├── urls.py                  # URLs principales
│   ├── wsgi.py                  # Configuración WSGI
│   └── asgi.py                  # Configuración ASGI
├── core/                        # App principal
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/core/
│   │   └── home.html            # Página principal
│   └── static/home/
│       └── home.css
├── products/                    # Gestión de productos
│   ├── models.py                # Modelo Product
│   ├── views.py                 # Vistas CRUD
│   ├── forms.py                 # Formularios
│   ├── urls.py
│   ├── admin.py
│   ├── migrations/
│   ├── templates/products/
│   │   ├── product_list.html
│   │   ├── product_detail.html
│   │   └── product_create.html
│   └── static/product-list/
├── sales/                       # Sistema de ventas
│   ├── models.py                # Modelos Sale y SaleItem
│   ├── views.py                 # APIs y vistas de venta
│   ├── urls.py
│   ├── migrations/
│   └── templates/sales/
│       └── create_sale.html     # Interfaz de ventas
├── templates/                   # Templates globales
│   └── registration/
│       └── login.html
└── tienda_barcode/             # Entorno virtual
```

## Modelos de Datos

### Modelo Product
**Ubicación**: `products/models.py`

```python
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    stock = models.IntegerField(default=0, verbose_name="Stock")
    barcode = models.CharField(max_length=100, unique=True, verbose_name="Código de Barras")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")
```

**Características**:
- `barcode`: Campo único para identificación por código de barras
- `stock`: Control de inventario
- Timestamps automáticos para auditoría
- Validaciones de precio y stock no negativos

### Modelo Sale
**Ubicación**: `sales/models.py`

```python
class Sale(models.Model):
    sale_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Venta")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="Monto Total")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Vendedor")
```

### Modelo SaleItem
```python
class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items', verbose_name="Venta")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Producto")
    quantity = models.IntegerField(default=1, verbose_name="Cantidad")
    price_at_sale = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio al Vender")
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Subtotal")
```

**Relaciones**:
- Sale → User (Many-to-One)
- Sale → SaleItem (One-to-Many)
- SaleItem → Product (Many-to-One)

### Diagrama de Relaciones
```
User ────┐
         │ 1:N
         ▼
        Sale ────┐
                 │ 1:N
                 ▼
            SaleItem ────┐
                         │ N:1
                         ▼
                      Product
```

## Funcionalidades Principales

### 1. Gestión de Productos

#### Crear Producto
- **Vista**: `product_create` en `products/views.py`
- **Método**: Generación automática de códigos de barras
- **Algoritmo**: 
  ```python
  base_barcode = slugify(product.name)[:50]
  unique_id = str(uuid.uuid4()).split('-')[0]
  product.barcode = f"PROD-{base_barcode}-{unique_id}".upper()
  ```

#### Listar Productos
- **Vista**: `product_list`
- **Funcionalidades**: Visualización completa, búsqueda, filtros

#### Validaciones
- Nombres únicos de productos (AJAX)
- Códigos de barras únicos automáticos
- Precios y stock no negativos

### 2. Sistema de Ventas

#### Interfaz de Venta
**Archivo**: `sales/templates/sales/create_sale.html`

**Características**:
- Input para escáner de códigos de barras
- Carrito de compras dinámico
- Cálculo automático de totales
- Validación de stock en tiempo real

#### Flujo de Venta
1. **Escaneo**: Usuario escanea código de barras
2. **Búsqueda**: Sistema busca producto en BD
3. **Validación**: Verificación de stock disponible
4. **Carrito**: Adición al carrito temporal (JavaScript)
5. **Proceso**: Envío de carrito completo al backend
6. **Transacción**: Procesamiento atómico en base de datos

#### APIs de Venta

##### Buscar Producto por Código de Barras
```http
POST /sales/add_product/
Content-Type: application/json

{
    "barcode": "PROD-PRODUCTO-EJEMPLO-ABC123"
}
```

**Respuesta**:
```json
{
    "success": true,
    "product": {
        "id": 1,
        "name": "Producto Ejemplo",
        "price": 25.50,
        "stock": 100
    }
}
```

##### Completar Venta
```http
POST /sales/complete_sale/
Content-Type: application/json

{
    "cart": [
        {
            "id": 1,
            "name": "Producto A",
            "price": 25.50,
            "quantity": 2
        },
        {
            "id": 2,
            "name": "Producto B",
            "price": 15.00,
            "quantity": 1
        }
    ]
}
```

## API Endpoints

### Productos
```
GET  /products/                    # Listar productos
GET  /products/<id>/              # Detalle de producto
POST /products/create/            # Crear producto (solo admin)
GET  /products/check-unique/      # Validar nombre único (AJAX)
```

### Ventas
```
GET  /sales/new/                  # Interfaz de venta
POST /sales/add_product/          # Buscar producto por código de barras
POST /sales/complete_sale/        # Procesar venta completa
```

### Autenticación
```
GET  /login/                      # Página de login
POST /login/                      # Procesar login
GET  /logout/                     # Cerrar sesión
```

## Sistema de Autenticación

### Usuarios y Roles
- **Django User Model**: Sistema de usuarios integrado
- **Superuser**: Propietario (acceso completo)
- **Staff**: Empleados (solo ventas)

### Decoradores de Seguridad
```python
@login_required                   # Requiere autenticación
@user_passes_test(is_owner)      # Solo propietarios
@csrf_exempt                     # APIs específicas
```

### Control de Acceso
- **Productos**: Solo propietarios pueden crear/modificar
- **Ventas**: Usuarios autenticados
- **Admin**: Solo superusuarios

## Frontend y UX

### Framework CSS
**Tailwind CSS**: Framework de utilidades para diseño rápido y responsive

### Componentes JavaScript

#### Gestión de Carrito
```javascript
let currentCart = [];           // Array de productos
let scannedProduct = null;      // Producto actual escaneado

function updateCartUI() {
    // Actualiza interfaz del carrito
    // Calcula totales
    // Gestiona botones
}
```

#### Comunicación AJAX
```javascript
fetch('/sales/add_product/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCsrfToken()
    },
    body: JSON.stringify({ barcode: barcode })
})
```

### Funcionalidades UX
- **Autofocus**: Input de código de barras siempre activo
- **Mensajes modales**: Feedback inmediato al usuario
- **Carrito dinámico**: Actualización en tiempo real
- **Validaciones**: Verificación de stock antes de añadir

## Configuración y Deployment

### Settings Principales
**Archivo**: `tienda_project/settings.py`

```python
# Seguridad
DEBUG = True                     # Solo desarrollo
ALLOWED_HOSTS = ["192.168.18.25", "127.0.0.1", "localhost"]
CSRF_TRUSTED_ORIGINS = ["https://7869d06dbeea.ngrok-free.app"]

# Apps
INSTALLED_APPS = [
    'core',
    'products', 
    'sales',
    'js_practice'
]

# Base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Autenticación
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
```

### Variables de Entorno
- **TIME_ZONE**: 'America/Lima'
- **LANGUAGE_CODE**: 'en-us'
- **SECRET_KEY**: Clave secreta Django

## Consideraciones de Seguridad

### Implementadas
- **CSRF Protection**: Tokens en formularios AJAX
- **SQL Injection**: Uso de Django ORM
- **Authentication**: Decoradores @login_required
- **Authorization**: Control de acceso por roles

### Transacciones Atómicas
```python
with transaction.atomic():
    # Crear venta
    # Crear items
    # Actualizar stock
    # Si algo falla, revierte todo
```

### Validaciones
- Stock suficiente antes de venta
- Códigos de barras únicos
- Nombres de productos únicos
- Precios no negativos

## Guía de Instalación

### ⚠️ IMPORTANTE
**Para una guía de instalación completa y detallada, consultar el archivo [GUIA_INSTALACION.md](./GUIA_INSTALACION.md)**

### Instalación Rápida (Resumen)

#### Prerrequisitos
- Python 3.10+
- pip (gestor de paquetes)
- Git (opcional)

#### Pasos Básicos

1. **Clonar repositorio**:
```bash
git clone https://github.com/Urarara01/django-effective-codebar-sales.git
cd django-effective-codebar-sales
```

2. **Crear entorno virtual**:
```bash
python -m venv tienda_barcode
# Windows:
tienda_barcode\Scripts\activate
# Linux/Mac:
source tienda_barcode/bin/activate
```

3. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

4. **Configurar base de datos**:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario**:
```bash
python manage.py createsuperuser
```

6. **Ejecutar servidor**:
```bash
python manage.py runserver
```

### URLs Principales
- **Home**: `http://127.0.0.1:8000/`
- **Productos**: `http://127.0.0.1:8000/products/`
- **Ventas**: `http://127.0.0.1:8000/sales/new/`
- **Reportes**: `http://127.0.0.1:8000/products/report-of-the-day/`
- **Admin**: `http://127.0.0.1:8000/admin/`

### Datos de Prueba
Para testing, crear productos usando la interfaz web:
1. Acceder a `/products/create/` (requiere login como superusuario)
2. Crear productos de prueba con nombres descriptivos
3. Los códigos de barras se generan automáticamente
4. Usar `/sales/new/` para probar el sistema de ventas

## Mejoras Futuras Sugeridas

### Funcionalidades
- Reportes de ventas y analytics
- Sistema de devoluciones
- Integración con impresoras de recibos
- Soporte para múltiples tipos de códigos de barras
- Sistema de descuentos y promociones

### Técnicas
- Migración a PostgreSQL para producción
- Implementación de Redis para caché
- API REST completa con Django REST Framework
- Testing automatizado
- Dockerización
- Deployment en servicios cloud

### UX/UI
- Progressive Web App (PWA)
- Modo offline básico
- Soporte para múltiples idiomas
- Dashboard de administración mejorado
- Notificaciones push

---

**Documentación generada**: Octubre 2025  
**Versión del proyecto**: 1.0  
**Framework**: Django 5.2.7  
**Autor**: [Tu nombre/equipo]  
**Repositorio**: django-effective-codebar-sales