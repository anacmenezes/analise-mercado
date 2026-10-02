from pathlib import Path

import chromadb
from chromadb.utils import embedding_functions


DOCUMENTS_PATH = Path("data/documents")
CHROMA_PATH = "data/chroma"


def create_vector_store():
    client = chromadb.PersistentClient(
        path=CHROMA_PATH
    )

    embedding_function = embedding_functions.DefaultEmbeddingFunction()

    collection = client.get_or_create_collection(
        name="market_analysis",
        embedding_function=embedding_function
    )

    documents = []
    metadatas = []
    ids = []

    for file in DOCUMENTS_PATH.glob("*.txt"):
        content = file.read_text(encoding="utf-8")

        documents.append(content)

        metadatas.append({
            "source": file.name
        })

        ids.append(file.stem)

    if documents:
        collection.upsert(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

    return collection


if __name__ == "__main__":
    collection = create_vector_store()

    print(
        f"Documentos indexados: {collection.count()}"
    )