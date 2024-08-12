from uuid import uuid4
from fastapi import HTTPException

from bson import ObjectId
from bson.errors import InvalidId


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


async def _check_exists_poll(question: str) -> Poll:
    poll = await poll_collection.find_one({"question": question})
    return poll["_id"] if poll else False


async def get_poll_result(poll_id: str) -> Poll:
    try:
        poll_id = ObjectId(poll_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail='poll_id is not valid, poll_id must be 24 character')
    else:
        poll = await poll_collection.find_one({"_id": poll_id})
        if poll:
            poll["id"] = str(poll["_id"])
            return Poll(**poll)
