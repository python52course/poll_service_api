import asyncio
import os

import motor
import pytest
from motor.core import AgnosticClient

from config.settings import settings

os.environ["MODE"] = "TEST"


@pytest.fixture(autouse=True)
async def connection_db():
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
