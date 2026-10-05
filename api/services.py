from sqlalchemy.orm import Session

from src.market_analysis.crew import criar_crew
from .models import Analise


def gerar_analise(sector: str, db: Session):

    crew = criar_crew()

    resultado = crew.kickoff(
        inputs={
            "sector": sector
        }
    )

    analise = Analise(
        sector=sector,
        relatorio=resultado.raw
    )

    db.add(analise)
    db.commit()
    db.refresh(analise)

    return analise

def atualizar_analise(analise_id: int, sector: str, db: Session):

    analise = db.query(Analise).filter(
        Analise.id == analise_id
    ).first()

    if not analise:
        return None

    analise.sector = sector

    db.commit()
    db.refresh(analise)

    return analise


def deletar_analise(analise_id: int, db: Session):

    analise = db.query(Analise).filter(
        Analise.id == analise_id
    ).first()

    if not analise:
        return False

    db.delete(analise)
    db.commit()

    return True