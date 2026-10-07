from crewai_tools import SerperDevTool
from crewai.tools import tool

from ..rag.retriever import search


search_tool = SerperDevTool()


@tool("Busca na base de conhecimento")
def rag_search(query: str) -> str:
    """
    Busca informações relevantes na base de conhecimento
    utilizando RAG.
    """

    results = search(query)

    if not results:
        return "Nenhuma informação relevante encontrada na base de conhecimento."

    formatted_results = []

    for result in results:
        content = result["content"]
        metadata = result["metadata"]

        formatted_results.append(
            f"Fonte: {metadata['source']}\n"
            f"Conteúdo:\n{content}"
        )

    return "\n\n---\n\n".join(formatted_results)