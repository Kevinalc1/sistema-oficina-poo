from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from services import carro_service

class CarroInput(BaseModel):
    modelo: str
    placa: str
    dono: str
    problema: str 

router = APIRouter(prefix="/carros", tags=["Carros"])

@router.post("/")
def criar_carro(carro_data: CarroInput, db: Session = Depends(get_db)):
    try:
        carro = carro_service.criar_carro(
            db, 
            modelo=carro_data.modelo, 
            placa=carro_data.placa, 
            dono=carro_data.dono,
            problema=carro_data.problema 
        )
        return carro
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/")
def listar_carros(db: Session = Depends(get_db)):
    return carro_service.listar_carros(db)