#database\database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

#cargar los archivos de .env
load_dotenv()

#Extrae el valor de la URL de la base de datos para conectar.
DATABASE_URL = os.getenv("DATABASE_URL")

#Crea el "motor" de conexión a la base de datos PostgreSQL.
engine = create_engine(DATABASE_URL)
#Crea una sesión para ejecutar consultas (como un cursor en SQL).
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Clase base de SQLAlchemy para crear los modelos de las tablas
Base = declarative_base()

# Dependencia para obtener la sesión
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()