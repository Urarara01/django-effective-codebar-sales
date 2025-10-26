# 📱 Guía de Instalación para Termux

## 🤖 Sistema de Automatización de Tienda - Termux Edition

Esta guía te ayudará a instalar y ejecutar el proyecto Django en Termux (Android).

### 📋 Requisitos Previos

1. **Termux App** instalada desde F-Droid o Google Play
2. **Acceso a internet** (solo para instalación inicial)
3. **Al menos 2GB de espacio libre**

### 🚀 Instalación Rápida

#### Paso 1: Preparar Termux
```bash
# Actualizar paquetes de Termux
pkg update && pkg upgrade -y

# Instalar dependencias básicas
pkg install python git -y

# Verificar instalación
python --version
```

#### Paso 2: Obtener el Proyecto
```bash
# Clonar repositorio
git clone https://github.com/Urarara01/django-effective-codebar-sales.git

# Navegar al directorio
cd django-effective-codebar-sales

# Dar permisos al script de Termux
chmod +x run_termux.sh
```

#### Paso 3: Instalación Automática
```bash
# Ejecutar instalación completa
./run_termux.sh full

# O paso a paso:
./run_termux.sh install  # Instalar dependencias
./run_termux.sh setup    # Configurar BD
./run_termux.sh run      # Ejecutar servidor
```

### 🎯 Uso Diario

#### Ejecutar el Servidor
```bash
# Navegar al proyecto
cd django-effective-codebar-sales

# Ejecutar servidor
./run_termux.sh run

# Ejecutar en puerto específico
./run_termux.sh run 8080
```

#### Acceder a la Aplicación
- **En el mismo dispositivo**: http://127.0.0.1:8000/
- **Desde otros dispositivos**: http://[IP_DEL_CELULAR]:8000/

### ⚠️ Diferencias con la Versión PC

#### Funcionalidades Offline
- ✅ **Sin CDN**: Estilos embebidos para funcionar sin internet
- ✅ **Templates optimizados**: Diseño específico para móviles
- ✅ **Detección automática**: El sistema detecta si está en Termux

#### Limitaciones
- ❌ **Sin gráficos Chart.js**: Reemplazados por listas simples
- ⚠️ **Rendimiento**: Más lento que en PC por limitaciones de hardware
- ⚠️ **Batería**: Uso intensivo de batería al ejecutar servidor

### 🔧 Configuraciones Específicas

#### Variables de Entorno
```bash
# En ~/.bashrc o ejecutar manualmente
export DJANGO_SETTINGS_MODULE='tienda_project.settings_termux'
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
```

#### Configuración de Red
```bash
# Encontrar IP del dispositivo
ip route get 8.8.8.8 | grep -oP 'src \K[^ ]+'

# Configurar ALLOWED_HOSTS (automático en settings_termux.py)
```

### 🛠️ Solución de Problemas

#### Error: "Permission denied"
```bash
chmod +x run_termux.sh
termux-setup-storage  # Si necesitas acceso al almacenamiento
```

#### Error: "No module named django"
```bash
pip install django python-slugify
```

#### Error: "Address already in use"
```bash
# Cambiar puerto
./run_termux.sh run 8001

# O matar proceso
pkill -f "python.*runserver"
```

#### Performance lento
```bash
# Usar configuración optimizada
export DJANGO_SETTINGS_MODULE='tienda_project.settings_termux'

# Limpiar caché
python manage.py clearsessions
```

### 📊 Características Optimizadas para Termux

#### Interface Móvil-First
- **Diseño responsive** nativo
- **Touch-friendly** botones y elementos
- **Modo oscuro** automático
- **Sin dependencias externas**

#### Optimizaciones de Rendimiento
- **Caché en memoria** habilitado
- **Queries optimizadas**
- **Assets mínimos**
- **Logging simplificado**

### 🔐 Seguridad en Termux

#### Configuración Básica
```bash
# Cambiar puerto por defecto
./run_termux.sh run 9000

# Restringir acceso solo local
# (modificar ALLOWED_HOSTS en settings_termux.py)
```

#### Consejos de Seguridad
- ✅ **No exponer** a internet pública
- ✅ **Usar solo en WiFi** privada
- ✅ **Cerrar servidor** cuando no uses
- ✅ **Backup regular** de db.sqlite3

### 📱 Optimización para Batería

#### Reducir Consumo
```bash
# Modo de bajo consumo (reducir workers)
export DJANGO_DEBUG=False

# Parar servidor cuando no uses
Ctrl+C

# Usar en modo airplane + WiFi solo cuando sea necesario
```

### 🤝 Acceso desde Otros Dispositivos

#### Configurar Red Local
```bash
# Ejecutar servidor para red
./run_termux.sh run

# El script automáticamente configurará la IP
# Acceder desde otro dispositivo: http://192.168.X.X:8000/
```

#### Usando ngrok (Opcional)
```bash
# Instalar ngrok en Termux
pkg install golang
go install github.com/inconshreveable/ngrok@latest

# Exponer servidor
~/go/bin/ngrok http 8000
```

### 📂 Estructura de Archivos en Termux

```
/data/data/com.termux/files/home/
└── django-effective-codebar-sales/
    ├── run_termux.sh              # Script principal
    ├── tienda_project/
    │   └── settings_termux.py     # Configuración Termux
    ├── products/templates/products/
    │   └── report_of_the_day_termux.html  # Template offline
    └── db.sqlite3                 # Base de datos
```

### 🆘 Comandos Útiles

```bash
# Estado del servidor
ps aux | grep python

# Logs del sistema
tail -f django.log

# Espacio libre
df -h

# Procesos de red
netstat -tulpn | grep :8000

# Reiniciar Termux completamente
exit  # Cerrar y abrir Termux
```

### 🎉 ¡Listo!

Ahora tienes un sistema completo de punto de venta funcionando en tu celular Android. 

**Ventajas del modo Termux:**
- ✅ **Portabilidad total**
- ✅ **No requiere PC**
- ✅ **Funciona offline** (después de instalación)
- ✅ **Acceso desde múltiples dispositivos**

**¡Perfecto para pequeños negocios móviles!** 🚀📱