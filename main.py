import sys

from src.market_analysis.crew import criar_crew


def main():

    sector = (
        sys.argv[1]
        if len(sys.argv) > 1
        else "Inteligência Artificial"
    )

    try:
        crew = criar_crew()

        resultado = crew.kickoff(
            inputs={
                "sector": sector
            }
        )

        print("\n===== RESULTADO FINAL =====\n")
        print(resultado)

    except Exception as erro:
        print("\n===== ERRO NA EXECUÇÃO =====")
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()