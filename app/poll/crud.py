from typing import Optional
from uuid import uuid4

from common.utils import convert_to_bson_object_id
from core.database import poll_collection
from poll.schemas import CreatePoll, Poll


async def get_poll_by_question(question: str) -> Optional[str]:
    """
    Get a poll by question.

    Args:
        question (str): The question of the poll.

    Returns:
        Optional[str]: The ID of the poll if it exists, otherwise None.
    """
    poll = await poll_collection.find_one({"question": question})
    return poll["_id"] if poll else None


async def get_poll_by_id(poll_id: str) -> Optional[Poll]:
    """
    Get a poll by ID.

    Args:
        poll_id (str): The ID of the poll.

    Returns:
        Optional[Poll]: The poll if it exists, otherwise None.

    Raises:
        exceptions.ObjectIdNotValidException: If the poll_id is not valid.
    """
    poll_id = convert_to_bson_object_id(poll_id)
    poll = await poll_collection.find_one({"_id": poll_id})
    if poll:
        poll["id"] = str(poll["_id"])
        return Poll(**poll)
    return None


async def create_poll(poll: CreatePoll) -> Poll:
    """
    Create a new poll.

    Args:
        poll (CreatePoll): The poll to create.

    Returns:
        Poll: The created poll.
    """
    poll_data = {
        "question": poll.question,
        "choices": [
            {"id": str(uuid4())[:6], "text": choice, "votes": 0} for choice in poll.choices
        ],
    }
    result = await poll_collection.insert_one(poll_data)
    poll_data["id"] = str(result.inserted_id)
    return Poll(**poll_data)


async def update_vote_in_poll(poll_id: str, choice_id: str) -> Optional[Poll]:
    """
    Update the vote in a poll.

    Args:
        poll_id (str): The ID of the poll.
        choice_id (str): The ID of the choice.

    Returns:
        Optional[Poll]: The updated poll if the choice exists, otherwise None.

    Raises:
        exceptions.ObjectIdNotValidException: If the poll_id is not valid.
    """
    poll_id = convert_to_bson_object_id(poll_id)
    poll = await poll_collection.find_one({"_id": poll_id})
    if poll:
        for choice in poll["choices"]:
            if choice["id"] == choice_id:
                choice["votes"] += 1
                break
        else:
            return None
        await poll_collection.update_one({"_id": poll_id}, {"$set": {"choices": poll["choices"]}})
        poll["id"] = str(poll["_id"])
        return Poll(**poll)
    return None
