from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import get_db
from .models import Analise
from .schemas import (
    AnaliseCreate,
    AnaliseResponse,
    AnaliseUpdate
)
from .services import gerar_analise
from .services import (
    gerar_analise,
    atualizar_analise,
    deletar_analise
)

router = APIRouter()

@router.post("/analises", response_model=AnaliseResponse)
def criar_analise(
    request: AnaliseCreate,
    db: Session = Depends(get_db)
):
    
    return gerar_analise(request.sector, db)

@router.get("/analises", response_model=list[AnaliseResponse])
def listar_analises(db: Session = Depends(get_db)):

    return db.query(Analise).all()


@router.get("/analises/{analise_id}", response_model=AnaliseResponse)
def buscar_analise(
    analise_id: int,
    db: Session = Depends(get_db)
):

    analise = db.query(Analise).filter(
        Analise.id == analise_id
    ).first()

    if not analise:
        raise HTTPException(
            status_code=404,
            detail="Análise não encontrada"
        )

    return analise


@router.put("/analises/{analise_id}", response_model=AnaliseResponse)
def atualizar(
    analise_id: int,
    request: AnaliseUpdate,
    db: Session = Depends(get_db)
):
    analise = atualizar_analise(
        analise_id,
        request.sector,
        db
    )

    if not analise:
        raise HTTPException(
            status_code=404,
            detail="Análise não encontrada"
        )

    return analise

@router.delete("/analises/{analise_id}")
def deletar(
    analise_id: int,
    db: Session = Depends(get_db)
):
    sucesso = deletar_analise(analise_id, db)

    if not sucesso:
        raise HTTPException(
            status_code=404,
            detail="Análise não encontrada"
        )

    return {
        "message": "Análise excluída com sucesso"
    }