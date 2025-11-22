from sqlalchemy import Column, Integer, String
from app.database import Base

class Carro(Base):
    __tablename__ = "carros"

    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String, nullable=False)
    placa = Column(String, unique=true, nullable=False)
    dono = Column(String, nullable=False)
    problema = Column(String)