# Se Necesitan tener los permisos de seguridad configurados con Set-ExecutionPolicy RemoteSigned
# para ello abrir la consola de PowerShell como administrador y ejecutar:
# Set-ExecutionPolicy RemoteSigned

# Crear el entorno virtual si no existe
if (!(Test-Path -Path ".\.venv")) {
    python -m venv .venv
}

# Activar el entorno virtual
& ".\.venv\Scripts\Activate.ps1"

# Descargar dependencias
pip3 install -r requirements.txt