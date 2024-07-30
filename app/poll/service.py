from uuid import uuid4

from config.database import poll_collection
from poll.schemas import CreatePoll, Poll


async def create_poll(poll: CreatePoll) -> Poll:
    poll_data = {
        "question": poll.question,
        "choices": [
            {"id": str(uuid4())[:6], "text": choice, "votes": 0} for choice in poll.choices
        ],
    }
    result = await poll_collection.insert_one(poll_data)
    poll_data["id"] = str(result.inserted_id)
    return Poll(**poll_data)


async def check_exists_poll(question: str) -> Poll:
    poll = await poll_collection.find_one({"question": question})
    return poll["_id"] if poll else False
