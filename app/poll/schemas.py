from typing import List

from pydantic import BaseModel, Field, field_validator


class Choice(BaseModel):
    """
    A choice for a poll.

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
    A poll.

    Attributes:
        id (str): The ID of the poll.
        question (str): The question of the poll.
        choices (List[Choice]): The choices for the poll.
    """

    id: str
    question: str
    choices: List[Choice]


class CreatePoll(BaseModel):
    """
    A poll to create.

    Attributes:
        question (str): The question of the poll.
        choices (List[str]): The choices for the poll.

    Methods:
        validate_question: Validates the question.
        validate_choices: Validates the choices.
    """

    question: str = Field(description="Question")
    choices: List[str] = Field(description="Poll options")

    @field_validator("question")
    def validate_question(cls, value: str) -> str:
        """
        Validates the question.

        Args:
            value (str): The question.

        Returns:
            str: The validated question.

        Raises:
            ValueError: If the question is empty.
        """
        if not value:
            raise ValueError("Question can not be empty")
        return value.strip()

    @field_validator("choices")
    def validate_choices(cls, value: list) -> List[Choice]:
        """
        Validates the choices.

        Args:
            value (list): The choices.

        Returns:
            List[Choice]: The validated choices.

        Raises:
            ValueError: If the choices are empty or if there are less than 2 unique choices.
        """
        if not value:
            raise ValueError("Poll options can not be empty")
        if len(set(value)) < 2:
            raise ValueError("Poll options must be more than 1 unique options")
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "question": "What is your favorite Pokemon?",
                "choices": ["Pikachu", "Charmander", "Squirting"],
            },
        }
