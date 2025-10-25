# 🛒 Guía de Instalación - Sistema de Automatización de Tienda con Código de Barras

## 📋 Tabla de Contenidos
1. [Requisitos Previos](#requisitos-previos)
2. [Instalación Paso a Paso](#instalación-paso-a-paso)
3. [Configuración Inicial](#configuración-inicial)
4. [Primer Uso](#primer-uso)
5. [Verificación de la Instalación](#verificación-de-la-instalación)
6. [Solución de Problemas](#solución-de-problemas)
7. [Configuración para Producción](#configuración-para-producción)

## 🔧 Requisitos Previos

### Software Requerido
- **Python 3.10 o superior** 
  - [Descargar Python](https://www.python.org/downloads/)
  - Verificar instalación: `python --version`
- **Git** (opcional, para clonar el repositorio)
  - [Descargar Git](https://git-scm.com/downloads/)
- **Editor de código** (recomendado: VS Code, PyCharm)

### Verificar Instalación de Python
```bash
python --version
# Debe mostrar: Python 3.10.x o superior

pip --version
# Debe mostrar la versión de pip
```

## 🚀 Instalación Paso a Paso

### Paso 1: Obtener el Código del Proyecto

#### Opción A: Clonar desde Git (Recomendado)
```bash
git clone https://github.com/Urarara01/django-effective-codebar-sales.git
cd django-effective-codebar-sales
```

#### Opción B: Descargar ZIP
1. Descargar el archivo ZIP del proyecto
2. Extraer en la carpeta deseada
3. Abrir terminal/cmd en la carpeta extraída

### Paso 2: Crear Entorno Virtual

#### En Windows (PowerShell/CMD)
```powershell
# Crear entorno virtual
python -m venv tienda_barcode

# Activar entorno virtual
tienda_barcode\Scripts\activate

# Verificar activación (debe aparecer (tienda_barcode) al inicio)
```

#### En macOS/Linux
```bash
# Crear entorno virtual
python3 -m venv tienda_barcode

# Activar entorno virtual
source tienda_barcode/bin/activate

# Verificar activación (debe aparecer (tienda_barcode) al inicio)
```

### Paso 3: Instalar Dependencias

```bash
# Asegurarse de que el entorno virtual esté activado
# Debe aparecer (tienda_barcode) al inicio de la línea

# Instalar dependencias
pip install -r requirements.txt

# Verificar instalación
pip list
```

### Paso 4: Configurar la Base de Datos

```bash
# Crear migraciones iniciales
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Verificar que se creó db.sqlite3
```

### Paso 5: Crear Usuario Administrador

```bash
python manage.py createsuperuser

# Seguir las instrucciones:
# Username: tu_usuario
# Email: tu_email@ejemplo.com
# Password: tu_contraseña_segura
```

### Paso 6: Iniciar el Servidor

```bash
python manage.py runserver

# El servidor iniciará en: http://127.0.0.1:8000/
```

## ⚙️ Configuración Inicial

### 1. Verificar Configuraciones en settings.py

El archivo `tienda_project/settings.py` ya tiene configuraciones básicas, pero revisa:

```python
# Configuración de zona horaria (ajustar según tu ubicación)
TIME_ZONE = 'America/Lima'  # Cambiar según tu zona horaria

# Para desarrollo local
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# Para acceso desde red local (opcional)
ALLOWED_HOSTS = ["192.168.x.x", "127.0.0.1", "localhost"]
```

### 2. Configuración de Hosts (Opcional)

Si quieres acceder desde otros dispositivos en tu red local:

```python
# En settings.py, modificar ALLOWED_HOSTS
ALLOWED_HOSTS = ["tu_ip_local", "127.0.0.1", "localhost"]

# Ejemplo:
ALLOWED_HOSTS = ["192.168.1.100", "127.0.0.1", "localhost"]

# Luego ejecutar:
python manage.py runserver 0.0.0.0:8000
```

## 🎯 Primer Uso

### 1. Acceder al Sistema

1. **Página Principal**: http://127.0.0.1:8000/
2. **Login**: http://127.0.0.1:8000/login/
3. **Admin Panel**: http://127.0.0.1:8000/admin/

### 2. Crear Productos de Prueba

1. **Iniciar sesión** con tu usuario administrador
2. **Ir a Productos**: http://127.0.0.1:8000/products/
3. **Crear nuevo producto**:
   - Nombre: "Coca Cola 500ml"
   - Descripción: "Bebida gaseosa"
   - Precio: 2.50
   - Stock: 100
   - El código de barras se genera automáticamente

4. **Crear más productos** para tener variedad de prueba

### 3. Probar el Sistema de Ventas

1. **Ir a Ventas**: http://127.0.0.1:8000/sales/new/
2. **Escanear código de barras** o escribirlo manualmente
3. **Agregar productos al carrito**
4. **Completar venta**

### 4. Ver Reportes

1. **Ir al reporte del día**: http://127.0.0.1:8000/products/report-of-the-day/
2. **Verificar estadísticas de ventas**

## ✅ Verificación de la Instalación

### Checklist de Verificación

- [ ] ✅ Python 3.10+ instalado
- [ ] ✅ Entorno virtual activado
- [ ] ✅ Dependencias instaladas
- [ ] ✅ Base de datos migrada
- [ ] ✅ Superusuario creado
- [ ] ✅ Servidor ejecutándose sin errores
- [ ] ✅ Página principal carga correctamente
- [ ] ✅ Login funciona
- [ ] ✅ Crear productos funciona
- [ ] ✅ Sistema de ventas funciona

### Comandos de Verificación

```bash
# Verificar estado del proyecto
python manage.py check

# Verificar migraciones pendientes
python manage.py showmigrations

# Verificar usuario creado
python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.all()
>>> exit()
```

## 🔧 Solución de Problemas

### Error: "Python no se reconoce como comando"
**Solución**: Agregar Python al PATH del sistema o usar `py` en lugar de `python`

### Error: "No module named 'django'"
**Solución**: 
```bash
# Verificar que el entorno virtual esté activado
pip install django
```

### Error: "Port already in use"
**Solución**:
```bash
# Usar puerto diferente
python manage.py runserver 8001

# O encontrar proceso usando puerto 8000
netstat -ano | findstr :8000  # Windows
lsof -ti:8000 | xargs kill -9  # macOS/Linux
```

### Error: "CSRF Token Missing"
**Solución**: Verificar que las plantillas incluyan `{% csrf_token %}` en formularios

### Error de Migraciones
**Solución**:
```bash
# Resetear migraciones (⚠️ CUIDADO: borra datos)
python manage.py migrate --fake-initial
# O eliminar db.sqlite3 y repetir paso 4
```

### Error: "Static files not found"
**Solución**:
```bash
python manage.py collectstatic
```

## 🌐 Configuración para Producción

### 1. Variables de Entorno

Crear archivo `.env`:
```bash
DEBUG=False
SECRET_KEY=tu_clave_secreta_muy_larga_y_segura
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com
DATABASE_URL=postgresql://usuario:password@localhost/nombre_bd
```

### 2. Base de Datos PostgreSQL (Recomendado para producción)

```bash
pip install psycopg2-binary

# En settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'tienda_db',
        'USER': 'tienda_user',
        'PASSWORD': 'tu_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 3. Servidor Web (Nginx + Gunicorn)

```bash
pip install gunicorn

# Crear archivo gunicorn.conf.py
bind = "127.0.0.1:8000"
workers = 3
```

### 4. Configuraciones de Seguridad

```python
# En settings.py para producción
DEBUG = False
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SECURE_HSTS_SECONDS = 86400
```

## 📱 Configuración para Acceso Móvil

### 1. Configurar para Red Local

```python
# En settings.py
ALLOWED_HOSTS = ["*"]  # Solo para desarrollo
# O específicamente:
ALLOWED_HOSTS = ["192.168.1.100", "127.0.0.1", "localhost"]
```

### 2. Ejecutar en Red

```bash
# Encontrar tu IP local
ipconfig  # Windows
ifconfig  # macOS/Linux

# Ejecutar servidor
python manage.py runserver 0.0.0.0:8000

# Acceder desde móvil: http://192.168.1.100:8000/
```

## 📞 Soporte y Contacto

### Recursos Adicionales
- [Documentación Django](https://docs.djangoproject.com/)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Python Official Docs](https://docs.python.org/)

### Estructura de Archivos Importantes
```
proyecto/
├── manage.py              # Comando principal Django
├── requirements.txt       # Dependencias Python
├── db.sqlite3            # Base de datos (se crea automáticamente)
├── tienda_project/       # Configuración principal
│   └── settings.py       # Configuraciones del proyecto
├── core/                 # App principal (home)
├── products/             # Gestión de productos
├── sales/                # Sistema de ventas
└── templates/            # Plantillas HTML globales
```

## 🎉 ¡Instalación Completada!

Si has seguido todos los pasos, deberías tener:

1. ✅ **Sistema funcionando** en http://127.0.0.1:8000/
2. ✅ **Productos creados** y visibles
3. ✅ **Sistema de ventas operativo**
4. ✅ **Códigos de barras generándose automáticamente**
5. ✅ **Reportes del día funcionando**

### Próximos Pasos
1. **Personalizar configuraciones** según tus necesidades
2. **Agregar productos reales** de tu inventario
3. **Capacitar usuarios** en el uso del sistema
4. **Configurar backups** regulares
5. **Considerar migración a producción** cuando esté listo

---

**¿Problemas con la instalación?** 
- Verificar que Python 3.10+ esté instalado
- Asegurar que el entorno virtual esté activado
- Revisar la sección de solución de problemas
- Consultar logs de error para diagnosticar issues específicos

**¡Listo para automatizar tu tienda! 🚀**