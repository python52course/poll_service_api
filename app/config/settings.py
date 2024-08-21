from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Variables from .env"""

    HOST: str
    API_PORT: int
    MONGODB_URL: str

    model_config = ConfigDict(extra="allow")


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
server_url = f"{settings.HOST}:{settings.API_PORT}"
