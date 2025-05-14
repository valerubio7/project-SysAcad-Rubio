from alembic.config import Config
from alembic import command

def run_migrations():
    try:
        print("Iniciando migraciones manualmente...")

        # Configurar Alembic
        alembic_cfg = Config("migrations/alembic.ini")

        # Ejecutar las migraciones
        command.upgrade(alembic_cfg, "head")
        print("Migraciones aplicadas exitosamente.")

    except Exception as e:
        print(f"Error al aplicar las migraciones: {e}")

if __name__ == "__main__":
    run_migrations()