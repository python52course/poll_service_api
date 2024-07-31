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
    question: str = Field(description="Вопрос")
    choices: List[str] = Field(description="Варианты голосования")

    @field_validator("question")
    def validate_question(cls, value: str):
        if not value.strip():
            raise ValueError("Вопрос не может быть пустым")
        return value

    @field_validator("choices")
    def validate_choices(cls, value: list):
        if len(value) < 2:
            raise ValueError("Варианты голосования не могут быть пустыми")
        return value

    class Config:
        json_schema_extra = {
            "example": {
                "question": "Какой ваш любимый покемон?",
                "choices": ["Пикачу", "Чармандер", "Сквиртл"],
            },
        }
