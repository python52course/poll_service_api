from fastapi import HTTPException, status

# PollAllReadyExistsException = HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail="The poll already exists, check the poll_id",
#         )


PollDoesNotExistsException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND, detail="The poll was not found"
)

OptionDoesNotExistsException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST, detail="There is no such answer option"
)


ObjectIdNotValidException = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="poll_id is not valid, poll_id must be 24 character",
)
