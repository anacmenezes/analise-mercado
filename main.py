import time

from src.market_analysis.crew import criar_crew
from src.market_analysis.observability.logger import logger
from src.market_analysis.observability.metrics import registrar_execucao
from src.market_analysis.observability.error_handler import registrar_erro


def main():

    logger.info("Iniciando análise de mercado")

    inicio = time.time()
    try:
        crew = criar_crew()

        logger.info("Crew criada")

        resultado = crew.kickoff(
            inputs={
                "sector": "Inteligência Artificial"
            }
        )

        registrar_execucao(resultado, inicio)

        print("\n===== RESULTADO FINAL =====\n")
        print(resultado)

    except Exception as erro:

        registrar_erro("execução da Crew", erro)

        print("\nErro durante a execução da análise.")
        print("Consulte o arquivo logs/market_analysis.log")


if __name__ == "__main__":
    main()