from crewai import Agent

from ..tools.search_tool import search_tool


def criar_pesquisador():

    return Agent(
        role="Pesquisador de Mercado",

        goal=(
            "Coletar e organizar informações relevantes e atualizadas "
            "sobre {sector}, utilizando fontes confiáveis."
        ),

        backstory="""
        Você é um pesquisador experiente especializado em análise de mercado.

        Seu trabalho é pesquisar informações atualizadas sobre {sector},
        identificar dados relevantes, tendências, empresas e estatísticas.

        Sempre que precisar de informações atuais, utilize a ferramenta
        de pesquisa disponível.
        """,

        tools=[search_tool],

        allow_delegation=False,

        verbose=True
    )