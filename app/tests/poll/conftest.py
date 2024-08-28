from typing import Any, AsyncGenerator, Dict, Tuple

import pytest
from httpx import AsyncClient

from core.config import server_url
from main import app


@pytest.fixture
async def async_session() -> AsyncGenerator[AsyncClient, None]:
    """
    A pytest fixture to create an asynchronous client for testing.

    Returns:
        AsyncGenerator[AsyncClient, None]: A generator that yields the asynchronous client.
    """
    async with AsyncClient(app=app, base_url=f"{server_url}/api") as session:
        yield session


@pytest.fixture
async def create_poll_fixture(
    request: pytest.FixtureRequest,
    async_session: AsyncClient,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """
    A pytest fixture to create a poll.

    Args:
        request (pytest.FixtureRequest): The pytest fixture request.
        async_session (AsyncClient): The asynchronous client.

    Returns:
        Tuple[Dict[str, Any], Dict[str, Any]]: A tuple containing the response and the data.
    """
    data = request.param
    response = await async_session.post("/createPoll/", json=data)
    return response.json(), data
