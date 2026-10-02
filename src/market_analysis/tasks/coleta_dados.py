from crewai import Task


def criar_coleta_dados(pesquisador):

    return Task(
        description=(
            "Realize uma pesquisa completa sobre {sector}.\n\n"

            "PRIMEIRO, consulte obrigatoriamente a base de conhecimento "
            "interna utilizando a ferramenta de RAG.\n\n"

            "Registre explicitamente quais informações foram encontradas "
            "na base interna e suas respectivas fontes.\n\n"

            "DEPOIS, utilize a ferramenta de pesquisa na internet para "
            "complementar as informações com dados atuais.\n\n"

            "Identifique:\n"
            "1. Principais empresas e participantes do mercado.\n"
            "2. Tendências atuais.\n"
            "3. Dados e estatísticas relevantes.\n"
            "4. Oportunidades e desafios.\n"
            "5. Informações encontradas na base de conhecimento.\n"
            "6. Fontes internas utilizadas.\n"
            "7. Fontes externas utilizadas.\n\n"

            "É OBRIGATÓRIO separar claramente:\n"
            "- INFORMAÇÕES DA BASE INTERNA (RAG)\n"
            "- INFORMAÇÕES DA INTERNET\n\n"

            "Para cada informação da base interna, informe o nome do "
            "arquivo utilizado como fonte.\n\n"

            "Não invente dados ou fontes."
        ),

        expected_output=(
            "Um documento estruturado contendo obrigatoriamente:\n"
            "- informações da base interna;\n"
            "- fontes internas, identificadas pelos nomes dos arquivos;\n"
            "- informações atuais encontradas na internet;\n"
            "- tendências;\n"
            "- empresas;\n"
            "- dados e estatísticas;\n"
            "- oportunidades e desafios;\n"
            "- fontes externas utilizadas."
        ),

        agent=pesquisador
    )