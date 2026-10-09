from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status

from app.schemas import DocumentUploadResponse
from app.services.chunking import chunk_text
from app.services.ollama_clinet import OllamaClient, get_ollama_client
from app.services.vector_store import VectorStore, get_vector_store


router = APIRouter(prefix="/documents", tags=["documents"])

ALLOWED_EXTENSION = {".txt", ".md"}


@router.post("/upload", response_model=DocumentUploadResponse, status_code=status.HTTP_201_CREATED)
async def upload_document(
    file: UploadFile = File(...),
    ollama: OllamaClient = Depends(get_ollama_client),
    store: VectorStore = Depends(get_vector_store)
) -> DocumentUploadResponse:
    extension = "." + file.filename.rsplit(".", 1)[-1].lower() if "." in file.filename else ""
    if extension not in ALLOWED_EXTENSION:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Unsupported file type '{extension}'. Allowed: {sorted(ALLOWED_EXTENSION)}",
        )