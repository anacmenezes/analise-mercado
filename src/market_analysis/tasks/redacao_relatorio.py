from crewai import Task


def criar_redacao_relatorio(redator, contexto):

    return Task(

        description=(
            "Elabore o relatório final utilizando exclusivamente as "
            "informações fornecidas pelo Pesquisador e pelo Analista.\n\n"

            "Preserve a distinção entre informações provenientes da "
            "base de conhecimento interna (RAG) e informações encontradas "
            "na internet.\n\n"

            "As fontes internas NÃO podem ser descartadas.\n"
            "Inclua os nomes dos arquivos utilizados pelo RAG no campo "
            "fontes_internas.\n\n"

            "Organize o relatório de forma clara e profissional."
        ),

        expected_output=(
            "Um relatório de análise de mercado em formato Markdown, "
            "contendo contexto, empresas, tendências, estatísticas, "
            "oportunidades, desafios, fontes_internas e fontes_externas."
        ),

        agent=redator,

        context=[contexto]
    )