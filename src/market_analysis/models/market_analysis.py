from typing import List
from pydantic import BaseModel


class MarketAnalysis(BaseModel):
    contexto: str
    empresas: List[str]
    tendencias: List[str]
    estatisticas: List[str]
    oportunidades: List[str]
    desafios: List[str]
    fontes_internas: List[str]
    fontes_externas: List[str]