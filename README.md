# 🛒 Sistema de Automatización de Tienda con Código de Barras

Sistema web desarrollado en Django para automatizar ventas en tiendas mediante códigos de barras. Incluye gestión de productos, sistema de ventas, control de inventario y reportes en tiempo real.

## 🚀 Inicio Rápido

### Instalación
```bash
# Clonar repositorio
git clone https://github.com/Urarara01/django-effective-codebar-sales.git
cd django-effective-codebar-sales

# Crear entorno virtual
python -m venv tienda_barcode
tienda_barcode\Scripts\activate  # Windows
# source tienda_barcode/bin/activate  # macOS/Linux

# Instalar dependencias
pip install -r requirements.txt

# Configurar base de datos
python manage.py migrate

# Crear usuario administrador
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
```

### Acceso
- **Aplicación**: http://127.0.0.1:8000/
- **Panel Admin**: http://127.0.0.1:8000/admin/

## 📋 Características

- ✅ **Gestión de Productos**: CRUD completo con códigos de barras automáticos
- ✅ **Sistema de Ventas**: Escáner de códigos de barras y carrito dinámico
- ✅ **Control de Inventario**: Actualización automática de stock
- ✅ **Reportes**: Dashboard con estadísticas del día
- ✅ **Autenticación**: Sistema de usuarios con roles diferenciados
- ✅ **Responsive**: Diseño adaptable para móviles y tablets

## 🛠️ Tecnologías

- **Backend**: Django 5.2.7, Python 3.10+
- **Frontend**: HTML5, CSS3, Tailwind CSS, JavaScript
- **Base de Datos**: SQLite3 (desarrollo), PostgreSQL (producción)
- **Códigos de Barras**: Generación automática con Code128

## 📚 Documentación

- **[Guía de Instalación Completa](./GUIA_INSTALACION.md)** - Instalación paso a paso
- **[Documentación Técnica](./DOCUMENTACION_TECNICA.md)** - Arquitectura y desarrollo

## 🎯 Funcionalidades Principales

### Gestión de Productos
- Crear, editar, eliminar productos
- Generación automática de códigos de barras
- Validación de nombres únicos
- Control de stock

### Sistema de Ventas
- Escáner de códigos de barras
- Carrito de compras dinámico
- Validación de stock en tiempo real
- Procesamiento de ventas atómico

### Reportes y Analytics
- Dashboard del día
- Ventas por hora
- Productos más vendidos
- Alertas de stock bajo

## 🖥️ Capturas de Pantalla

### Página Principal
![Home](docs/screenshots/home.png)

### Lista de Productos
![Products](docs/screenshots/products.png)

### Sistema de Ventas
![Sales](docs/screenshots/sales.png)

### Reportes del Día
![Reports](docs/screenshots/reports.png)

## 🔧 Configuración

### Desarrollo
```python
# settings.py
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
```

### Producción
```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ["tu-dominio.com"]
# Configurar base de datos PostgreSQL
# Configurar archivos estáticos
```

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👥 Autores

- **Urarara01** - *Desarrollo inicial* - [Urarara01](https://github.com/Urarara01)

## 🙏 Agradecimientos

- Django por el excelente framework
- Tailwind CSS por el sistema de diseño
- La comunidad de Python por las herramientas

## 📞 Soporte

¿Tienes problemas o preguntas?
- 📖 Consulta la [Documentación](./DOCUMENTACION_TECNICA.md)
- 🚀 Revisa la [Guía de Instalación](./GUIA_INSTALACION.md)
- 🐛 Reporta bugs en [Issues](https://github.com/Urarara01/django-effective-codebar-sales/issues)

---

⭐ **¡Si te gusta este proyecto, danos una estrella!** ⭐