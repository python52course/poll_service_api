import os

from motor.motor_asyncio import AsyncIOMotorClient

from config.settings import settings

client = AsyncIOMotorClient(settings.mongodb_url)


def get_database():
    """prepare database"""

    TEST_MODE = os.getenv("MODE") == "TEST"
    if TEST_MODE:
        db = client.get_database("test_poll_database")
        poll_collection = db.get_collection("test_poll_collection")
    else:
        db = client.get_database("poll_database")
        poll_collection = db.get_collection("poll_collection")
    return db, poll_collection


db, poll_collection = get_database()