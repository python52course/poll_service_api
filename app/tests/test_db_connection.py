import pytest

from app.config.database import client


@pytest.mark.asyncio
async def test_db_connection() -> None:
    """test connection with Database"""

    connection = await client.server_info()
    assert connection
