import os

from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(os.environ["MONGODB_URL"])


if os.getenv("MODE") == "TEST":
    db = client.get_database("test_poll_database")
    poll_collection = db.get_collection("test_poll_collection")
else:
    db = client.get_database("poll_database")
    poll_collection = db.get_collection("poll_collection")
