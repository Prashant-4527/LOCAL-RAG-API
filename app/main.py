from fastapi import FastAPI

from app.config import settings
from app.schemas import HealthResponse

app = FastAPI(
    titel=settings.app_name,
    description="Chat with your own documents - 100% local, 100% free.",
    version="0.1.0"
)


@app.get("/health", response_model=HealthResponse, tags=["system"])
async def health_check() -> HealthResponse:
    return {"status": "ok", "message": "API is running."}

