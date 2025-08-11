from sqlalchemy import Column, Integer, String
from database import Base

class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(30),nullable=False, index=True)
    telefono = Column(Integer, nullable=False, index=True)
    email = Column(String, unique=True, index= True, nullable=False)
    direccion = Column(String, index=True, nullable=False)

