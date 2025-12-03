from fastapi import FastAPI
from app.database import Base, engine
from app.controllers.carro_controller import router as carro_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API da Oficina",version="1.0.0",description="API para cadastro e gerenciamento de carros")

app.include_router(carro_router)

@app.get("/") 
def root():return {"message": "API da Oficina está rodando!"} 