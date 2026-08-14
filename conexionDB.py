'''
Archivo de configuración de la base de datos PostgreSQL usando SQLAlchemy.

'''

from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase

# Definicion del esquema para los modelos
class Base(DeclarativeBase):
    pass

# Variables para la conexion con la base
DATABASE_USER = "postgres"
DATABASE_PASSWORD = "48704342004"
DATABASE_HOST = "localhost"
DATABASE_PORT = "5432"
DATABASE_NAME = "postgres"

# URL para la conexion
DATABASE_URL = (
    f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}"
    f"@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)

# Creacion del engine
engine = create_engine(DATABASE_URL)

# Devuelve el engine configurado para la base de datos
def get_engine():
    return engine

# Devuelve una conexión a la base de datos
def get_connection():
    return engine.connect()

# Test de conexion
if __name__ == "__main__":
    with engine.connect() as conn:
        version = conn.execute(text("SELECT version()")).scalar()
        print(f"Conexión exitosa: {version}")
