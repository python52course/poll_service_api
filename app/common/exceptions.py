from fastapi import HTTPException, status

from common.exc_enums import ExceptionMessages


class PollAlreadyExistsException(HTTPException):
    """
    Exception raised when a poll already exists.

    Args:
        detail (str): The detail of the exception.
    """

    def __init__(self, detail: str) -> None:
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"{ExceptionMessages.PollAllReadyExistsException.value} {detail}",
        )


class PollDoesNotExistsException(HTTPException):
    """
    Exception raised when the poll does not exist.
    """

    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=ExceptionMessages.PollDoesNotExistsException.value,
        )


class OptionDoesNotExistsException(HTTPException):
    """
    Exception raised when the option does not exist.
    """

    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ExceptionMessages.OptionDoesNotExistsException.value,
        )


class ObjectIdNotValidException(HTTPException):
    """
    Exception raised when the object ID is not valid.
    """

    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=ExceptionMessages.ObjectIdNotValidException.value,
        )
