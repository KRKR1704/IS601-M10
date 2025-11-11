# Author: Roopesh Kumar Reddy Kaipa
# Date: 11/10/2025
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:postgres@localhost:5432/fastapi_db"
    
    class Config:
        env_file = ".env"

settings = Settings()