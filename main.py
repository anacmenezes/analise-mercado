from src.market_analysis.crew import criar_crew
from src.market_analysis.evaluation.evaluator import (
    avaliar_task,
    avaliar_qualidade
)



def main():

    crew = criar_crew()

    resultado = crew.kickoff(
        inputs={
            "sector": "Inteligência Artificial"
        }
    )

    print("\n===== RESULTADO FINAL =====\n")
    print(resultado)

    criterios = [
        {
            "fontes": ["Fonte", "Fontes"],
            "dados": ["dados", "estatísticas"],
            "tendencias": ["tendências"],
        },
        {
            "tendencias": ["tendências"],
            "oportunidades": ["oportunidades"],
            "desafios": ["desafios"],
        },
        {
            "estrutura": ["Introdução", "Conclusão"],
            "fontes": ["Fontes Internas", "Fontes Externas"],
        }
    ]

    print("\n===== AVALIAÇÃO DOS AGENTES =====\n")

    for i, task_output in enumerate(resultado.tasks_output):

        avaliacao = avaliar_task(
            task_output,
            criterios[i]
        )

        print(f"Task {i + 1}")

        for criterio, passou in avaliacao["criterios"].items():
            status = "OK" if passou else "FALHOU"
            print(f"- {criterio}: {status}")

        print(f"Score: {avaliacao['score']}/10")

    print("\n===== AVALIAÇÃO DE QUALIDADE =====\n")

    qualidade = avaliar_qualidade(resultado.tasks_output[-1])

    for criterio, passou in qualidade["criterios"].items():
        status = "OK"  if passou else "FALHOU"
        print(f"- {criterio}: {status}")

if __name__ == "__main__":
    main()