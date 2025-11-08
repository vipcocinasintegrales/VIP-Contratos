import sys
import subprocess
import platform
import os
import time
import importlib

# ==============================
# 🧠 CONFIGURACIÓN BÁSICA
# ==============================
VERSION_MIN = (3, 8)
VERSION_MAX = (3, 12)
RUTA_VENV = "venv"
RUTA_REQUIREMENTS = "entorno/requirements.txt"
RUTA_APP = "app/principal.py"  # Archivo principal de la app

# ==============================
# 🔍 VERIFICAR PYTHON
# ==============================
def verificar_version_python():
    version_actual = sys.version_info
    print(f"\n🐍 Versión actual de Python: {version_actual.major}.{version_actual.minor}.{version_actual.micro}")

    if (version_actual.major, version_actual.minor) < VERSION_MIN or (version_actual.major, version_actual.minor) > VERSION_MAX:
        print("\n⚠️  La versión actual de Python NO es compatible con Streamlit.")
        print(f"   Se recomienda una versión entre {VERSION_MIN[0]}.{VERSION_MIN[1]} y {VERSION_MAX[0]}.{VERSION_MAX[1]}.")
        print("   Descárgala desde: https://www.python.org/downloads/\n")
        sys.exit(1)
    else:
        print("✅ Versión de Python compatible.\n")

# ==============================
# ⚙️ CREAR ENTORNO VIRTUAL
# ==============================
def crear_entorno_virtual():
    """Crea un entorno virtual si no existe."""
    if not os.path.exists(RUTA_VENV):
        print("⚙️ Creando entorno virtual...\n")
        subprocess.check_call([sys.executable, "-m", "venv", RUTA_VENV])
        print("✅ Entorno virtual creado correctamente.\n")
    else:
        print("🟢 El entorno virtual ya existe.\n")

# ==============================
# 🔧 ACTIVAR ENTORNO Y PIP
# ==============================
def activar_entorno():
    """Devuelve el ejecutable de Python dentro del entorno virtual."""
    if platform.system() == "Windows":
        return os.path.join(RUTA_VENV, "Scripts", "python.exe")
    else:
        return os.path.join(RUTA_VENV, "bin", "python")

# ==============================
# 📦 INSTALAR LIBRERÍAS SOLO SI FALTAN
# ==============================
def instalar_paquete_si_falta(python_exec, paquete):
    """Instala una librería solo si no está instalada."""
    nombre_modulo = paquete.split("==")[0]  # Ignora la versión al importar
    try:
        importlib.import_module(nombre_modulo)
        print(f"✅ {paquete} ya está instalada, se omite.")
    except ImportError:
        print(f"\n📦 Instalando {paquete}...\n")
        comando = [python_exec, "-m", "pip", "install", paquete]
        try:
            proceso = subprocess.Popen(comando, stdout=sys.stdout, stderr=sys.stderr)
            proceso.wait()
            if proceso.returncode == 0:
                print(f"✅ {paquete} instalado correctamente.\n")
            else:
                print(f"❌ Error al instalar {paquete}. Revisa los mensajes anteriores.\n")
        except Exception as e:
            print(f"❌ Error inesperado al instalar {paquete}: {e}\n")

def instalar_librerias(python_exec):
    """Lee el archivo requirements.txt e instala cada dependencia si falta."""
    print("🔍 Iniciando instalación de dependencias...\n")

    if not os.path.exists(RUTA_REQUIREMENTS):
        print(f"❌ No se encontró el archivo {RUTA_REQUIREMENTS}.")
        sys.exit(1)

    with open(RUTA_REQUIREMENTS, "r", encoding="utf-8") as f:
        librerias = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    for lib in librerias:
        instalar_paquete_si_falta(python_exec, lib)
        time.sleep(0.5)  # Pausa breve para claridad

    print("\n✅ Instalación completa de todas las librerías faltantes.\n")

# ==============================
# 🚀 INICIAR LA APP
# ==============================
def iniciar_app(python_exec):
    """Ejecuta la aplicación principal en Streamlit."""
    if os.path.exists(RUTA_APP):
        print("🚀 Iniciando la aplicación Streamlit...\n")
        subprocess.run([python_exec, "-m", "streamlit", "run", RUTA_APP])
    else:
        print(f"⚠️ No se encontró la aplicación principal en {RUTA_APP}. Crea el archivo para continuar.\n")

# ==============================
# 🧩 FUNCIÓN PRINCIPAL
# ==============================
def main():
    print("\n=== 🧩 Iniciador del Proyecto VIP-Contratos ===\n")

    verificar_version_python()
    crear_entorno_virtual()

    python_venv = activar_entorno()

    instalar_librerias(python_venv)
    iniciar_app(python_venv)

if __name__ == "__main__":
    main()
