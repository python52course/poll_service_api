from fastapi import APIRouter, status

import poll.crud as crud
from common import exceptions
from poll.schemas import CreatePoll, Poll

router = APIRouter(prefix="/api", tags=["Voting"])


@router.post(
    "/createPoll/",
    response_description="Create a new poll",
    status_code=status.HTTP_201_CREATED,
)
async def create_poll(poll: CreatePoll) -> Poll:
    """
    Create a new poll.

    Args:
        poll (CreatePoll): The poll to create.
    Returns:
        Poll: The created poll.
    Raises:
        exceptions.PollAlreadyExistsException: If a poll with the same question already exists.
    """
    existed_poll = await crud._check_exists_poll(poll.question)
    if existed_poll:
        raise exceptions.PollAlreadyExistsException(
            detail=f"{existed_poll}",
        )
    created_pool = await crud.create_poll(poll)
    return created_pool


@router.get("/getResult/{poll_id}/", response_description="Get the poll results")
async def get_result_poll(poll_id: str) -> Poll:
    """
    Get the results of a poll.

    Args:
        poll_id (str): The ID of the poll.
    Returns:
        Poll: The poll results.
    Raises:
        exceptions.PollDoesNotExistsException: If the poll does not exist.
    """
    poll = await crud.get_poll_results(poll_id)
    if poll:
        return poll
    raise exceptions.PollDoesNotExistsException


@router.post("/poll/", response_description="Vote for a specific option")
async def vote_for_specific_choice(poll_id: str, choice_id: str) -> Poll:
    """
    Vote for a specific option in a poll.

    Args:
        poll_id (str): The ID of the poll.
        choice_id (str): The ID of the option to vote for.
    Returns:
        Poll: The updated poll.
    Raises:
        exceptions.PollDoesNotExistsException: If the poll does not exist.
        exceptions.OptionDoesNotExistsException: If the option does not exist.
    """
    poll = await crud.get_poll_results(poll_id)
    if poll is None:
        raise exceptions.PollDoesNotExistsException
    updated_poll = await crud.update_vote_in_poll(poll_id, choice_id)
    if updated_poll is None:
        raise exceptions.OptionDoesNotExistsException
    return updated_poll
