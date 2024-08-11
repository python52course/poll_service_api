from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Variables from .env"""

    host: str
    api_port: int
    mongodb_url: str

    model_config = ConfigDict(extra="allow")


settings = Settings(_env_file=".env", _env_file_encoding="utf-8")
server_url = f"{settings.host}:{settings.api_port}"
