from fastapi import FastAPI

from api.routes import router
from api.database import Base, engine
from api import models


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Análise de Mercado - Multiagente",
    description="API de análise de mercado utilizando CrewAI, RAG e LLMs.",
    version="1.0.0"
)

app.include_router(router)