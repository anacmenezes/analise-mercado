from crewai import Agent


def criar_analista():
    return Agent(
        role="Analista de Tendências",
        goal="Analisar os dados do setor {sector} e identificar padrões e oportunidades",
        backstory="""
        Você é um analista de mercado que examina os dados coletados para identificar
        tendências emergentes, oportunidades e ameaças no setor {sector}.
        """,
        allow_delegation=False,
        verbose=True
    )