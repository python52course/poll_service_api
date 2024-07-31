import asyncio
import os

import motor
import pytest
from motor.core import AgnosticClient

os.environ["MODE"] = "TEST"


@pytest.fixture(scope="function")
async def connection_db():
    """
    Create a test database for use in tests.
    """

    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
    db = client.get_database("test_poll_database")
    AgnosticClient.get_io_loop = asyncio.get_running_loop
    await client.drop_database("test_poll_database")
    yield db
    await client.drop_database("test_poll_database")
    client.close()
