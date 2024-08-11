import pytest
from httpx import AsyncClient

from config.settings import server_url
from main import app


@pytest.fixture
async def async_session(connection_db):
    async with AsyncClient(app=app, base_url=f"{server_url}/api") as session:
        yield session
