# 📒 Agenda de Contactos – FastAPI

Proyecto CRUD de **Agenda de Contactos** desarrollado con **Python, FastAPI, SQLAlchemy y PostgreSQL**.

## 🚀 Funcionalidades
- Crear, leer, actualizar y eliminar contactos.
- Guardar nombre, teléfono, email y dirección.
- API documentada automáticamente con Swagger UI.

## 🛠 Tecnologías
- [Python 3](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)

## ▶️ Instalación y ejecución
```bash
# Clonar repositorio
git clone https://github.com/TU_USUARIO/agenda-contactos-fastapi.git

# Entrar en carpeta
cd agenda-contactos-fastapi

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
uvicorn app.main:app --reload
