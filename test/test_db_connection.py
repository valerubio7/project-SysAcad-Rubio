import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def test_db_connection():
    try:
        print("Iniciando prueba de conexión a la base de datos...")
        
        # Obtener la URI de la base de datos desde las variables de entorno
        database_uri = os.getenv('DEV_DATABASE_URI')
        print(f"DEV_DATABASE_URI: {database_uri}")
        if not database_uri:
            raise ValueError("La variable DEV_DATABASE_URI no está configurada.")

        # Crear el motor de conexión
        engine = create_engine(database_uri)

        # Probar la conexión
        print("Intentando conectar a la base de datos...")
        with engine.connect() as connection:
            print("Conexión exitosa a la base de datos.")

    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
    else:
        print("Prueba completada sin errores.")

if __name__ == "__main__":
    test_db_connection()