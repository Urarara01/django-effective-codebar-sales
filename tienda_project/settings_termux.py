# settings_termux.py - Configuración específica para Termux

from .settings import *
import os

# Configuración para Termux
ALLOWED_HOSTS = ['*']  # Permitir todos los hosts en Termux

# Configuración de timezone más flexible
TIME_ZONE = 'UTC'  # UTC es más compatible universalmente

# Base de datos con path absoluto más flexible
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {
            'timeout': 10,  # Timeout más largo para sistemas móviles
        }
    }
}

# Configuración de archivos estáticos para Termux
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configuración de seguridad más relajada para desarrollo en Termux
SECURE_BROWSER_XSS_FILTER = False
SECURE_CONTENT_TYPE_NOSNIFF = False

# Configuración de logging para debug en Termux
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# Configuración de caché simple para Termux
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

print("🤖 Configuración de Termux cargada")