from pydantic_settings import BaseSettings, SettingsConfigDict




class Settings(BaseSettings):
    app_name: str = "Local RAG API"
    app_version: str = "0.1.0"
    ollama_base_url: str = "http://localhost:11434"
    chat_model: str = "llama3.2"
    embedding_model: str = "nomic-embed-text"
    chroma_persist_dir: str = "./data/chroma"




    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()