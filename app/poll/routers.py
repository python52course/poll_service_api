from fastapi import APIRouter, HTTPException, status

import poll.crud as crud
from poll.schemas import CreatePoll, Poll

router = APIRouter(prefix="/api", tags=["Voting"])


@router.post(
    "/createPoll/",
    response_description="Create a new poll",
    status_code=status.HTTP_201_CREATED,
)
async def create_poll_handler(poll: CreatePoll) -> Poll:
    existed_poll = await crud._check_exists_poll(poll.question)
    if existed_poll:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"The poll already exists, check the poll_id {existed_poll}",
        )

    created_pool = await crud.create_poll(poll)
    return created_pool


@router.get("/getResult/{poll_id}/", response_description="Get the poll results")
async def get_result_poll_handler(poll_id: str) -> Poll:
    poll = await crud.get_poll_results(poll_id)
    if poll:
        return poll
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The poll not found")


@router.post("/poll/", response_description="Vote for a specific option")
async def vote_for_specific_choice(poll_id: str, choice_id: str) -> Poll:
    poll = await crud.get_poll(poll_id)
    if poll is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The poll was not found")
    updated_poll = await crud.update_vote_in_poll(poll_id, choice_id)
    if updated_poll is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="There is no such answer option"
        )
    return updated_poll
