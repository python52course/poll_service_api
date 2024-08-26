from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Variables from .env"""

    HOST: str
    API_PORT: int
    MONGODB_URL: str


settings = Settings()
server_url = f"{settings.HOST}:{settings.API_PORT}"
