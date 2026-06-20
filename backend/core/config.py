from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GROQ_API_KEY: str
    CHROMA_PATH: str = "./data/chroma"

    class Config:
        env_file = ".env"

settings = Settings()