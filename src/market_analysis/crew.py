from src.market_analysis.rag.ingest import create_vector_store
from src.market_analysis.rag.retriever import search


create_vector_store()

results = search(
    "Quais são as principais tendências de IA?"
)

for result in results:
    print("\n--- DOCUMENTO ---")
    print(result)