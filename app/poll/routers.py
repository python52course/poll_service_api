from fastapi import APIRouter, Body, HTTPException, status

import poll.crud as crud
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
        HTTPException: If the poll already exists.
    """
    existed_poll = await crud.get_poll_by_question(poll.question)
    if existed_poll:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"The poll already exists, check the poll_id {existed_poll}",
        )
    return await crud.create_poll(poll)


@router.post("/getResult/", response_description="Get the poll results")
async def get_poll_results(
    poll_id: str = Body(..., embed=True),
) -> Poll:
    """
    Get the results of a poll.

    Args:
        poll_id (str): The ID of the poll.

    Returns:
        Poll: The poll results.

    Raises:
        HTTPException: If the poll does not exist.
    """
    poll = await crud.get_poll_by_id(poll_id)
    if poll is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The poll was not found",
        )
    return poll


@router.post("/poll/", response_description="Vote for a specific option")
async def vote_for_specific_choice(
    poll_id: str = Body(..., embed=True),
    choice_id: str = Body(..., embed=True),
) -> Poll:
    poll = await crud.get_poll_by_id(poll_id)
    if poll is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="The poll was not found",
        )
    update_poll = await crud.update_vote_in_poll(poll_id, choice_id)
    if update_poll is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="There is no such answer option",
        )
    return update_poll
