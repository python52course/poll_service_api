from enum import Enum


class ExceptionMessages(Enum):
    PollAllReadyExistsException = "The poll already exists, check the poll_id"
    PollDoesNotExistsException = "The poll was not found"
    OptionDoesNotExistsException = "There is no such answer option"
    ObjectIdNotValidException = "poll_id is not valid, poll_id must be 24 character"
