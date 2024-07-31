from fastapi import APIRouter, HTTPException, status

import poll.service as service
from poll.schemas import CreatePoll, Poll

router = APIRouter(prefix="/api", tags=["Voting"])


@router.post(
    "/createPoll/",
    response_description="Create a new poll",
    status_code=status.HTTP_201_CREATED,
)
async def create_poll_handler(poll: CreatePoll) -> Poll:
    existed_poll = await service._check_exists_poll(poll.question)
    if existed_poll:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"The poll already exists, check the poll_id {existed_poll}",
        )

    created_pool = await service.create_poll(poll)
    return created_pool
