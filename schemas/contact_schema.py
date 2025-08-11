#schema\contact_schema.py

from pydantic import BaseModel, EmailStr

class ContactBase(BaseModel):
    nombre : str
    email : EmailStr
    telefono : int
    direccion : str

class ContactCreate(ContactBase):
    pass

class ContactResponse(ContactBase):
    id : int

    class Config :
        orm_mode = True


