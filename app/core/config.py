from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings.

    Attributes:
        HOST (str): The host to run the application on.
        API_PORT (int): The port to run the application on.
        MONGODB_URL (str): The MongoDB connection string.
    """

    HOST: str
    API_PORT: int
    MONGODB_URL: str


settings = Settings()
server_url = f"{settings.HOST}:{settings.API_PORT}"
