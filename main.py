import time

from src.market_analysis.crew import criar_crew
from src.market_analysis.observability.logger import logger
from src.market_analysis.observability.metrics import registrar_execucao


def main():

    logger.info("Iniciando análise de mercado")

    inicio = time.time()

    crew = criar_crew()

    resultado = crew.kickoff(
        inputs={
            "sector": "Inteligência Artificial"
        }
    )

    registrar_execucao(resultado, inicio)

    print("\n===== RESULTADO FINAL =====\n")
    print(resultado)


if __name__ == "__main__":
    main()