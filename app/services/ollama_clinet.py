import httpx
from app.config import settings


class OllamaClient:
    """Thin async wrapper around Ollama's local REST API."""

    def __init__(self, base_url: str = settings.ollama_vase_url):
        self._client = httpx.AsyncClient(base_url=base_url.rstrip("/"), timeout=60.0)


    async def embed(self, text: str) -> list[float]:
        response = await self._client.post(
            "/api/embeddings",
            json={"model": settings.embedding_model, "prompt": text},
        )

        response.raise_for_status()
        return response.json()["embedding"]


    async def close(self) -> None:
        await self._client.aclose()


ollama_client = OllamaClient()


def get_ollama_client() -> OllamaClient:
    """Dependency to get the OllamaClient instance."""
    return ollama_client


