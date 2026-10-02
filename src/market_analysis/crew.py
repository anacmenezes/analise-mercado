from crewai import Crew, Process

from .agents.pesquisador import criar_pesquisador
from .agents.analista import criar_analista
from .agents.redator import criar_redator

from .tasks.coleta_dados import criar_coleta_dados
from .tasks.analise_tendencias import criar_analise_tendencias
from .tasks.redacao_relatorio import criar_redacao_relatorio


def criar_crew():

    pesquisador = criar_pesquisador()
    analista = criar_analista()
    redator = criar_redator()

    coleta_dados = criar_coleta_dados(pesquisador)

    analise_tendencias = criar_analise_tendencias(
        analista,
        coleta_dados
    )

    redacao_relatorio = criar_redacao_relatorio(
        redator,
        analise_tendencias
    )

    return Crew(
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