from typing import Any, Dict

import pytest
from httpx import AsyncClient


@pytest.mark.parametrize(
    "data",
    [
        {
            "question": "What is your favorite programming language?",
            "choices": ["Python", "JavaScript", "Java", "Swift"],
        },
        {
            "question": "What is your preferred development environment?",
            "choices": ["Visual Studio Code", "PyCharm", "Sublime Text", "Atom"],
        },
        {
            "question": "What is your go-to database management system?",
            "choices": ["PostgreSQL", "MySQL", "MongoDB", "SQLite"],
        },
    ],
)
async def test_create_poll(
    async_session: AsyncClient,
    data: Dict[str, Any],
) -> None:
    response = await async_session.post("/createPoll/", json=data)
    response_data = response.json()
    assert response.status_code == 201
    assert response_data["question"] == data["question"]
    assert [choice["text"] for choice in response_data["choices"]] == data["choices"]
    assert response_data["choices"][0]["votes"] == 0


async def test_create_duplicate_poll(async_session: AsyncClient) -> None:
    data = {
        "question": "What is your favorite programming language?",
        "choices": ["Python", "JavaScript", "Java", "Swift"],
    }
    response = await async_session.post("/createPoll/", json=data)
    assert response.status_code == 201

    response = await async_session.post("/createPoll/", json=data)
    response_data = response.json()
    assert response.status_code == 409
    assert "The poll already exists, check the poll_id" in response_data["detail"]


@pytest.mark.parametrize(
    "data",
    [
        {"question": "", "choices": []},
        {"question": "What is your favorite color?", "choices": []},
        {
            "question": "",
            "choices": ["Gold", "Gold"],
        },
        {
            "question": "What is your favorite color?",
            "choices": ["Gold"],
        },
        {
            "question": "What is your favorite color?",
            "choices": ["Gold", "Gold"],
        },
        {},
    ],
)
async def test_for_invalid_input_returns_error_code(
    async_session: AsyncClient,
    data: Dict[str, Any],
) -> None:
    response = await async_session.post("/createPoll/", json=data)
    assert response.status_code == 422
