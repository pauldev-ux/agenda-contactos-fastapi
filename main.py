from fastapi import FastAPI

app = FastAPI(title='Agenda de Contactos')

@app.get('/')
async def read_root():
    return {"mensaje": "Bienvenido a la API de Agenda de Contactos"}

