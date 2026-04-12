from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str

    AZURE_OPENAI_KEY: str
    AZURE_OPENAI_ENDPOINT: str
    AZURE_OPENAI_GPT_MODEL_NAME: str
    AZURE_OPENAI_GPT_API_VERSION : str
    AZURE_OPENAI_EMBEDDING_MODEL_NAME: str
    AZURE_OPENAI_EMBEDDING_API_VERSION: str

    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
