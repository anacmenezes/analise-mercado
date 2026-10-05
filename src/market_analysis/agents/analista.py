from crewai import Agent
from ..config import MODEL_NAME

def criar_analista():
    return Agent(
        role="Analista de Tendências",
        goal="Analisar os dados do setor {sector} e identificar padrões e oportunidades",
        backstory="""
        Você é um analista de mercado que examina os dados coletados para identificar
        tendências emergentes, oportunidades e ameaças no setor {sector}.
        """,
        llm=MODEL_NAME,
        allow_delegation=False,
        verbose=True
    )