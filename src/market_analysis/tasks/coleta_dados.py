from crewai import Task


def criar_coleta_dados(pesquisador):

    return Task(
        description=(
            "Realize uma pesquisa completa sobre {sector}.\n\n"

            "Utilize as ferramentas disponíveis para coletar informações.\n\n"

            "Primeiro, consulte a base de conhecimento interna utilizando "
            "a ferramenta de RAG para identificar informações relevantes "
            "já disponíveis sobre o setor.\n\n"

            "Depois, utilize a ferramenta de pesquisa na internet para "
            "complementar a análise com informações atuais.\n\n"

            "Identifique:\n"
            "1. Principais empresas e participantes do mercado.\n"
            "2. Tendências atuais.\n"
            "3. Dados e estatísticas relevantes.\n"
            "4. Oportunidades e desafios.\n"
            "5. Informações encontradas na base de conhecimento.\n"
            "6. Fontes utilizadas.\n\n"

            "Diferencie informações provenientes da base interna das "
            "informações encontradas na internet.\n\n"

            "Não invente dados ou fontes."
        ),

        expected_output=(
            "Um documento estruturado contendo uma análise de {sector}, "
            "com tendências, empresas, dados, oportunidades, desafios "
            "e fontes utilizadas. O documento deve diferenciar informações "
            "provenientes da base interna e informações obtidas na internet."
        ),

        agent=pesquisador
    )