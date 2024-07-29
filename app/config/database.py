import os

from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(os.environ["MONGODB_URL"])

db = client.get_database("poll_database")
poll_collection = db.get_collection("poll_collection")
