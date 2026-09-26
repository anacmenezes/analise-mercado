from crewai import Agent


def criar_pesquisador():
    return Agent(
        role="Pesquisador de Mercado",
        goal="Coletar e organizar informações relevantes sobre {sector}",
        backstory="""
        Você é um pesquisador experiente que analisa tendências de mercado e coleta
        dados relevantes sobre {sector}. Seu trabalho é garantir que todas as
        informações estejam atualizadas e bem documentadas.
        """,
        allow_delegation=False,
        verbose=True
    )