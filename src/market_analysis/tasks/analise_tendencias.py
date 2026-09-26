from crewai import Task


def criar_analise_tendencias(analista, contexto):
    return Task(
        description=(
            "1. Examinar os dados coletados pelo Pesquisador de Mercado.\n"
            "2. Identificar padrões, tendências emergentes e oportunidades no setor {sector}.\n"
            "3. Elaborar uma análise detalhada destacando os principais pontos."
        ),
        expected_output=(
            "Um relatório com insights e tendências baseados nos dados do setor {sector}."
        ),
        agent=analista,
        context=contexto
    )