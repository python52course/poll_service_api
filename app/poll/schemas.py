from typing import List

from pydantic import BaseModel, Field, field_validator


class Choice(BaseModel):
    """
    Represents a choice in a poll.

    Attributes:
        id (str): The ID of the choice.
        text (str): The text of the choice.
        votes (int): The number of votes for the choice. Defaults to 0.
    """

    id: str
    text: str
    votes: int = 0


class Poll(BaseModel):
    """
    Represents a poll.

    Attributes:
        id (str): The ID of the poll.
        question (str): The question of the poll.
        choices (List[Choice]): The choices in the poll.
    """

    id: str
    question: str
    choices: List[Choice]


class CreatePoll(BaseModel):
    """
    Represents a poll to create.

    Attributes:
        question (str): The question of the poll.
        choices (List[str]): The choices in the poll.
    """

    question: str = Field(description="Question")
    choices: List[str] = Field(description="Poll options")

    @field_validator("question")
    def validate_question(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Question can not be empty")
        return value

    @field_validator("choices")
    def validate_choices(cls, value: List[Choice]) -> List[Choice]:
        if not value:
            raise ValueError("Poll options can not be empty")
        elif len(set(value)) < 2:
            raise ValueError("Poll options must be more than 1 unique options")
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "question": "What is your favorite Pokemon?",
                "choices": ["Pikachu", "Charmander", "Squirting"],
            },
        }
