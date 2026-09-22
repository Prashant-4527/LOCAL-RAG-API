import uuid

import chromadb
from chromadb.api.models.Collection import Collection

from app.config import settings


class VectorStore:
    """Wraps a persistent local ChromaDB collection."""

    def __init__(self, persist_dir: str = settings.chroma_persist_dir):
        self._client = chromadb.PersistentClient(path=persist_dir)
        self._collection: Collection = (
            self._client.get_or_create_collection(name="documents")
        )

    def add_chunks(
        self,
        chunks: list[str],
        embeddings: list[list[float]],
        source: str,
    ) -> list[str]:
        ids = [str(uuid.uuid4()) for _ in chunks]
        metadatas = [
            {"source": source, "chunk_index": i}
            for i in range(len(chunks))
        ]

        self._collection.add(
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
            ids=ids,
        )

        return ids

    def query(
        self,
        query_embedding: list[float],
        n_results: int = 4,
    ) -> dict:
        return self._collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
        )


vector_store = VectorStore()


def get_vector_store() -> VectorStore:
    return vector_store