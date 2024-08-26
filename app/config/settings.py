from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Variables from .env"""

    host: str
    api_port: int
    mongodb_url: str


settings = Settings()
server_url = f"{settings.host}:{settings.api_port}"
