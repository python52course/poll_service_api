from typing import Any, AsyncGenerator, Dict, Tuple

import pytest
from httpx import AsyncClient

from config.settings import server_url
from main import app


@pytest.fixture
async def async_session() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=app, base_url=f"{server_url}/api") as session:
        yield session


@pytest.fixture
async def create_poll_fixture(
    request: pytest.FixtureRequest,
    async_session: AsyncClient,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    data = request.param
    response = await async_session.post("/createPoll/", json=data)
    return response.json(), data
