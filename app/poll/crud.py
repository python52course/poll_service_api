from typing import Optional
from uuid import uuid4

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException, status

from config.database import poll_collection
from poll.schemas import CreatePoll, Poll


async def _check_exists_poll(question: str) -> Poll:
    poll = await poll_collection.find_one({"question": question})
    return poll["_id"] if poll else False


async def _validate_object_id(object_id):
    try:
        object_id = ObjectId(object_id)
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="poll_id is not valid, poll_id must be 24 character",
        )
    else:
        return object_id


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


async def get_poll_results(poll_id: str) -> Poll:
    poll_id = await _validate_object_id(poll_id)
    poll = await poll_collection.find_one({"_id": poll_id})
    if poll:
        poll["id"] = str(poll["_id"])
        return Poll(**poll)


async def get_poll(poll_id: str) -> Optional[Poll]:
    poll_id = await _validate_object_id(poll_id)
    poll = await poll_collection.find_one({"_id": poll_id})
    if poll:
        poll["id"] = str(poll["_id"])
        return Poll(**poll)


async def update_vote_in_poll(poll_id: str, choice_id: str) -> Optional[Poll]:
    poll_id = await _validate_object_id(poll_id)
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
