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

    return "\n\n".join(results)