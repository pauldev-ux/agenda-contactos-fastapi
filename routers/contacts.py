#routers\contacts.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from database.database import Base, get_db
from models.models import Contact
from schemas.contact_schema import ContactCreate, ContactResponse
from typing import List

router = APIRouter(prefix='/contacts', tags=['Contacts'])

@router.post('', response_model=ContactResponse)
async def create_contact(contact : ContactCreate, db : Session = Depends(get_db)):
    #verificar si el email existe
    existing_email = db.query(Contact).filter(Contact.email == contact.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="el email ya esta registrado")

    #crear contacto
    new_contact = Contact(**contact.model_dump())
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

@router.get('/',response_model=List[ContactResponse])
async def get_contacts(db : Session = Depends(get_db)):
    return db.query(Contact).all()

@router.get('/{contact_id}', response_model=ContactResponse)
async def get_contact(contact_id : int, db : Session = Depends(get_db)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact is None:
        raise HTTPException(status_code=404, detail="el contacto no existe")
    return contact

@router.put('/{contact_id}', response_model=ContactResponse)
async def update_contact(contact_id:int,update_contact:ContactCreate ,db:Session=Depends(get_db)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact is None:
        raise HTTPException(status_code=404, detail="el contacto no existe")

    #verificar si el nuevo email ya esta en uso
    if contact.email != update_contact.email:
        existing_email = db.query(Contact).filter(Contact.email == update_contact.email).first()
        if existing_email:
            raise HTTPException(status_code=400, detail="el email ya esta registrado")

    #actualizar los campos
    for key, value in update_contact.model_dump().items():
        setattr(contact, key, value)

    db.commit()
    db.refresh(contact)
    return contact


@router.delete('/{contact_id}')
async def delete_contact(contact_id : int, db : Session = Depends(get_db)):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact is None:
        raise HTTPException(status_code=404, detail="el contacto no existe")

    db.delete(contact)
    db.commit()
    return {"mensaje" : "contacto eliminado"}




