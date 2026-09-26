from crewai import Task


def criar_coleta_dados(pesquisador):
    return Task(
        description=(
            "1. Pesquisar e coletar informações atualizadas sobre {sector}.\n"
            "2. Identificar os principais players, tendências e estatísticas do setor.\n"
            "3. Organizar os dados de forma clara para análise."
        ),
        expected_output=(
            "Um documento estruturado contendo dados de mercado sobre {sector}."
        ),
        agent=pesquisador
    )