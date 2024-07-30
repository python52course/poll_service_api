import os

import motor.motor_asyncio
import pytest

os.environ["MODE"] = "TEST"


@pytest.fixture(scope='function')
async def connection_db():
    """
    Create a test database for use in tests.
    """

    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
    db = client.get_database("test_poll_database")
    await client.drop_database("test_poll_database")
    yield db
    await client.drop_database("test_poll_database")
    client.close()
