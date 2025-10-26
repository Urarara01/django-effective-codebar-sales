#!/data/data/com.termux/files/usr/bin/bash

# run_termux.sh - Script para ejecutar Django en Termux

echo "🤖 Iniciando Django en Termux..."

# Verificar que estamos en Termux
if [ -z "$PREFIX" ]; then
    echo "❌ Este script está diseñado para Termux"
    exit 1
fi

# Configurar variables de entorno para Termux
export DJANGO_SETTINGS_MODULE='tienda_project.settings_termux'
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Función para instalar dependencias si no existen
install_deps() {
    echo "📦 Verificando dependencias..."
    
    # Actualizar pkg si es necesario
    pkg update -y
    
    # Instalar Python si no está
    if ! command -v python &> /dev/null; then
        echo "🐍 Instalando Python..."
        pkg install python -y
    fi
    
    # Instalar pip dependencies
    if [ -f requirements.txt ]; then
        echo "📋 Instalando dependencias Python..."
        pip install -r requirements.txt
    fi
}

# Función para configurar la base de datos
setup_db() {
    echo "🗄️ Configurando base de datos..."
    
    if [ ! -f db.sqlite3 ]; then
        echo "🔧 Creando base de datos..."
        python manage.py makemigrations
        python manage.py migrate
        
        echo "👤 ¿Quieres crear un superusuario? (y/n)"
        read -r create_superuser
        if [ "$create_superuser" = "y" ] || [ "$create_superuser" = "Y" ]; then
            python manage.py createsuperuser
        fi
    else
        echo "✅ Base de datos ya existe"
        
        # Verificar si hay migraciones pendientes
        python manage.py showmigrations --plan | grep -q '\[ \]' && {
            echo "🔄 Aplicando migraciones pendientes..."
            python manage.py migrate
        }
    fi
}

# Función para obtener IP del dispositivo
get_device_ip() {
    # Intentar obtener IP wifi
    WIFI_IP=$(ip route get 8.8.8.8 2>/dev/null | grep -oP 'src \K[^ ]+' 2>/dev/null || echo "")
    
    if [ -n "$WIFI_IP" ]; then
        echo "$WIFI_IP"
    else
        echo "127.0.0.1"
    fi
}

# Función principal para ejecutar el servidor
run_server() {
    DEVICE_IP=$(get_device_ip)
    PORT=${1:-8000}
    
    echo "🌐 Iniciando servidor Django..."
    echo "📱 Accede desde este dispositivo: http://127.0.0.1:$PORT/"
    
    if [ "$DEVICE_IP" != "127.0.0.1" ]; then
        echo "🌍 Accede desde otros dispositivos: http://$DEVICE_IP:$PORT/"
    fi
    
    echo "🛑 Presiona Ctrl+C para detener el servidor"
    echo ""
    
    # Ejecutar servidor con configuración de Termux
    python manage.py runserver 0.0.0.0:$PORT --settings=tienda_project.settings_termux
}

# Verificar argumentos
case "$1" in
    "install")
        install_deps
        ;;
    "setup")
        setup_db
        ;;
    "run"|"")
        run_server $2
        ;;
    "full")
        install_deps
        setup_db
        run_server $2
        ;;
    *)
        echo "🤖 Uso: $0 [install|setup|run|full] [puerto]"
        echo ""
        echo "Comandos:"
        echo "  install  - Instalar dependencias"
        echo "  setup    - Configurar base de datos"
        echo "  run      - Ejecutar servidor (puerto por defecto: 8000)"
        echo "  full     - Hacer todo (install + setup + run)"
        echo ""
        echo "Ejemplos:"
        echo "  $0 full          # Configuración completa"
        echo "  $0 run 8080      # Ejecutar en puerto 8080"
        exit 1
        ;;
esac