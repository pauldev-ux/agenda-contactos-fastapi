from fastapi import FastAPI
from database import database
from models import models
from routers import contacts

#crear tablas en la base de datos
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title='Agenda de Contactos')


#incluir rutas
app.include_router(contacts.router)


@app.get('/')
async def read_root():
    return {"mensaje": "Bienvenido a la API de Agenda de Contactos"}

