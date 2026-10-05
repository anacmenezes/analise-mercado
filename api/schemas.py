from pydantic import BaseModel


class AnaliseCreate(BaseModel):
    sector: str


class AnaliseUpdate(BaseModel):
    sector: str


class AnaliseResponse(BaseModel):
    id: int
    sector: str
    relatorio: str

    class Config:
        from_attributes = True