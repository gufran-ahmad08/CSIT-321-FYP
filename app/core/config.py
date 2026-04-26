import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # The SQLite database URL for development
    DATABASE_URL: str = "sqlite:///./test.db"
    # Any other settings (like JWT secret key or others) can be added here later

    class Config:
        env_file = ".env"

# Initialize settings
settings = Settings()