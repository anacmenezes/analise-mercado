from crewai import Crew, Process

from .agents.pesquisador import criar_pesquisador
from .agents.analista import criar_analista
from .agents.redator import criar_redator

from .tasks.coleta_dados import criar_coleta_dados
from .tasks.analise_tendencias import criar_analise_tendencias
from .tasks.redacao_relatorio import criar_redacao_relatorio

from crewai import Task


def criar_crew():

    pesquisador = criar_pesquisador()
    analista = criar_analista()
    redator = criar_redator()

    coleta_dados = criar_coleta_dados(pesquisador)

    analise_tendencias = criar_analise_tendencias(
        analista,
        contexto=[coleta_dados]
    )

    redacao_relatorio = criar_redacao_relatorio(
        redator,
        contexto=[analise_tendencias]
    )

    crew = Crew(
        agents=[
            pesquisador,
            analista,
            redator
        ],
        tasks=[
            coleta_dados,
            analise_tendencias,
            redacao_relatorio
        ],
        process=Process.sequential,
        verbose=True
    )

    return crew

def criar_coleta_dados(pesquisador):

    return Task(
        description=(
            "Pesquise informações atualizadas sobre {sector} utilizando "
            "a ferramenta de pesquisa disponível.\n\n"

            "Identifique:\n"
            "1. Os principais participantes do mercado atualmente.\n"
            "2. Tendências observadas nos últimos 12 meses.\n"
            "3. Dados e estatísticas recentes.\n"
            "4. Oportunidades e desafios atuais.\n"
            "5. Fontes utilizadas para obter as informações.\n\n"

            "Priorize informações publicadas recentemente e fontes confiáveis.\n"
            "Não utilize dados anteriores a 2025 quando houver informações "
            "mais recentes disponíveis.\n"
            "Não invente dados ou fontes."
        ),

        expected_output=(
            "Um documento estruturado contendo informações atuais sobre "
            "{sector}, incluindo dados, tendências, principais participantes "
            "e as fontes utilizadas."
        ),

        agent=pesquisador
    )