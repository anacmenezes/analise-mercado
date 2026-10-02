from crewai import Task


def criar_redacao_relatorio(redator, contexto):
    return Task(
        description=(
            "1. Usar a análise de tendências para criar um relatório detalhado sobre {sector}.\n"
            "2. Garantir que o relatório seja bem estruturado e compreensível.\n"
            "3. Apresentar um resumo executivo e recomendações finais."
        ),
        expected_output=(
            "Um relatório de análise de mercado em formato Markdown, "
            "pronto para leitura e apresentação."
        ),
        agent=redator,
        context=[contexto]
    )