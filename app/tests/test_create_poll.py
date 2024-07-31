from httpx import AsyncClient

from config.settings import server_url
from main import app


async def test_create_poll(connection_db):
    data = {
        "question": "What is your favorite programming language?",
        "choices": ["Python", "JavaScript", "Java", "Swift"],
    }
    async with AsyncClient(app=app, base_url=f"{server_url}/api") as ac:
        response = await ac.post("/createPoll/", json=data)
    response_data = response.json()
    assert response.status_code == 201
    assert response_data["question"] == data["question"]
    assert len(response_data["choices"]) == len(data["choices"])
    assert response_data["choices"][0]["text"] == data["choices"][0]
    assert response_data["choices"][0]["votes"] == 0


async def test_create_duplicate_poll(connection_db):
    data = {
        "question": "What is your favorite programming language?",
        "choices": ["Python", "JavaScript", "Java", "Swift"],
    }
    async with AsyncClient(app=app, base_url=f"{server_url}/api") as ac:
        response = await ac.post("/createPoll/", json=data)
    async with AsyncClient(app=app, base_url=f"{server_url}/api") as ac:
        response = await ac.post("/createPoll/", json=data)
    response_data = response.json()
    assert response.status_code == 409
    assert "The poll already exists, check the poll_id" in response_data["detail"]


async def test_for_invalid_input_returns_error_code(connection_db):
    data = {
        "question": "",
        "choices": [],
    }
    async with AsyncClient(app=app, base_url=f"{server_url}/api") as ac:
        response = await ac.post("/createPoll/", json=data)
        assert response.status_code == 422


async def test_for_invalid_empty_input_returns_error_code(connection_db):
    async with AsyncClient(app=app, base_url=f"{server_url}/api") as ac:
        response = await ac.post("/createPoll/")
    assert response.status_code == 422
