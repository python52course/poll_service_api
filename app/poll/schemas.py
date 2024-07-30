from typing import List

from pydantic import BaseModel


class Choice(BaseModel):
    id: str
    text: str
    votes: int = 0


class Poll(BaseModel):
    id: str
    question: str
    choices: List[Choice]


class CreatePoll(BaseModel):
    question: str
    choices: List[str]

    class Config:
        json_schema_extra = {
            "example": {
                "question": "Какой ваш любимый покемон?",
                "choices": ["Пикачу", "Чармандер", "Сквиртл"],
            },
        }
