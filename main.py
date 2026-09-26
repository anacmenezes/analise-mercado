from src.market_analysis.crew import criar_crew


def main():

    crew = criar_crew()

    resultado = crew.kickoff(
        inputs={
            "sector": "Inteligência Artificial"
        }
    )

    print("\n===== RELATÓRIO FINAL =====\n")
    print(resultado)


if __name__ == "__main__":
    main()