from crewai import Agent


def criar_redator():
    return Agent(
        role="Redator de Relatórios",
        goal="Elaborar um relatório consolidado sobre a análise de mercado do setor {sector}.",
        backstory="""
        Você é um redator profissional que transforma análises de mercado em um relatório
        estruturado e compreensível para tomadores de decisão.
        """,
        allow_delegation=False,
        verbose=True
    )