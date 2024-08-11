from typing import List

from pydantic import BaseModel, Field, field_validator


class Choice(BaseModel):
    id: str
    text: str
    votes: int = 0


class Poll(BaseModel):
    id: str
    question: str
    choices: List[Choice]


class CreatePoll(BaseModel):
    question: str = Field(description="Question")
    choices: List[str] = Field(description="Poll options")

    @field_validator("question")
    def validate_question(cls, value: str):
        if not value.strip():
            raise ValueError("Question can not be empty")
        return value

    @field_validator("choices")
    def validate_choices(cls, value: list):
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
