from typing import Optional
from uuid import uuid4

from bson import ObjectId

from common import utils
from core.database import poll_collection
from poll.schemas import CreatePoll, Poll


async def _check_exists_poll(question: str) -> Optional[str]:
    poll = await poll_collection.find_one({"question": question})
    return poll["_id"] if poll else None


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


async def get_poll_results(poll_id: str) -> Optional[Poll]:
    poll_id = await utils.check_object_id(poll_id)
    poll = await poll_collection.find_one({"_id": poll_id})
    if poll:
        poll["id"] = str(poll["_id"])
        return Poll(**poll)


async def get_poll(poll_id: str) -> Optional[Poll]:
    poll_id = await utils.check_object_id(poll_id)
    poll = await poll_collection.find_one({"_id": poll_id})
    if poll:
        poll["id"] = str(poll["_id"])
        return Poll(**poll)


async def update_vote_in_poll(poll_id: str, choice_id: str) -> Optional[Poll]:
    poll_id = await utils.check_object_id(poll_id)
    poll = await poll_collection.find_one({"_id": ObjectId(poll_id)})
    if poll:
        for choice in poll["choices"]:
            if choice["id"] == choice_id:
                choice["votes"] += 1
                break
        else:
            return None
        await poll_collection.update_one(
            {"_id": ObjectId(poll_id)}, {"$set": {"choices": poll["choices"]}}
        )
        poll["id"] = str(poll["_id"])
        return Poll(**poll)
