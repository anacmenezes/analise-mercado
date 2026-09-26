from crewai import Task


def criar_coleta_dados(pesquisador):

    return Task(
        description=(
            "Pesquise informações atualizadas sobre {sector} utilizando "
            "a ferramenta de pesquisa disponível.\n\n"

            "Identifique:\n"
            "1. Principais empresas e participantes do mercado.\n"
            "2. Tendências atuais.\n"
            "3. Dados e estatísticas relevantes.\n"
            "4. Oportunidades e desafios.\n"
            "5. Fontes utilizadas para obter as informações.\n\n"

            "Priorize informações recentes e fontes confiáveis. "
            "Não invente dados ou fontes."
        ),

        expected_output=(
            "Um documento estruturado contendo informações atuais sobre "
            "{sector}, incluindo dados, tendências, principais participantes "
            "e as fontes utilizadas."
        ),

        agent=pesquisador
    )