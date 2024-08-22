from fastapi import HTTPException, status

from common.exc_enums import ExceptionMessages


class PollAlreadyExistsException(HTTPException):
    def __init__(self, detail: str) -> None:
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"{ExceptionMessages.PollAllReadyExistsException.value} {detail}",
        )


class ObjectIdNotValidException(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ExceptionMessages.ObjectIdNotValidException.value,
        )


class OptionDoesNotExistsException(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ExceptionMessages.OptionDoesNotExistsException.value,
        )


class PollDoesNotExistsException(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ExceptionMessages.PollDoesNotExistsException.value,
        )
