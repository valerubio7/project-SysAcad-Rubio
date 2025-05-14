from alembic.config import Config
from alembic import command

def test_alembic_connection():
    try:
        print("Iniciando prueba de conexión con Alembic...")

        # Configurar Alembic
        alembic_cfg = Config("migrations/alembic.ini")

        # Ejecutar un comando de prueba
        command.current(alembic_cfg)
        print("Conexión con Alembic exitosa.")

    except Exception as e:
        print(f"Error al conectar con Alembic: {e}")

if __name__ == "__main__":
    test_alembic_connection()