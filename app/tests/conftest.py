import asyncio
import os
from typing import AsyncGenerator

import motor
import pytest
from motor.core import AgnosticClient
from motor.motor_asyncio import AsyncIOMotorDatabase

from config.settings import settings

os.environ["MODE"] = "TEST"


@pytest.fixture(autouse=True)
async def connection_db() -> AsyncGenerator[AsyncIOMotorDatabase, None]:
    """
    Create a test database for use in tests.
    """

    client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_url)
    db = client.get_database("test_poll_database")
    AgnosticClient.get_io_loop = asyncio.get_running_loop
    await client.drop_database("test_poll_database")
    yield db
    await client.drop_database("test_poll_database")
    client.close()
