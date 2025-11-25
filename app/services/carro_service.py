from models.carro_model import Carro
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError 

def criar_carro(db: Session, modelo: str, placa: str, dono: str, problema: str):
    carro_existente = db.query(Carro).filter(Carro.placa == placa).first()

    if carro_existente:
        raise ValueError(f"A placa '{placa}' já está cadastrada para o carro de modelo {carro_existente.modelo}.")

    novo_carro = Carro(modelo=modelo, placa=placa, dono=dono, problema=problema)
    
    try:
        db.add(novo_carro)
        db.commit()
        db.refresh(novo_carro)
        return novo_carro
    except IntegrityError:
        db.rollback()
        raise ValueError("Erro de integridade. A placa pode ter sido cadastrada simultaneamente.")


def listar_carros(db: Session):
    return db.query(Carro).all()


def buscar_carro_por_placa(db: Session, placa: str):
    return db.query(Carro).filter(Carro.placa == placa).first()