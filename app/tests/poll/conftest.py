import pytest
from httpx import AsyncClient

from config.settings import server_url
from main import app


@pytest.fixture
async def async_session():
    async with AsyncClient(app=app, base_url=f"{server_url}/api") as session:
        yield session


@pytest.fixture
async def create_poll_fixture(request, async_session):
    data = {
        "question": "What is your favorite programming language?",
        "choices": ["Python", "JavaScript", "Java", "Swift"],
    }

    response = await async_session.post("/createPoll/", json=data)
    return response.json(), data
