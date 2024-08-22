from typing import Any, Dict, Tuple

import pytest
from fastapi import status
from httpx import AsyncClient

from common.exc_enums import ExceptionMessages


@pytest.mark.parametrize(
    "create_poll_fixture",
    [
        {
            "question": "What is your favorite programming language?",
            "choices": ["Python", "JavaScript", "Java", "Swift"],
        }
    ],
    indirect=True,
)
async def test_get_results_exists_poll(
    async_session: AsyncClient, create_poll_fixture: Tuple[Dict[str, Any], Dict[str, Any]]
) -> None:
    data = create_poll_fixture[1]
    poll_id = create_poll_fixture[0]["id"]
    response = await async_session.post(f"/getResult/?poll_id={poll_id}")
    response_data = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert response_data["id"] == poll_id
    assert response_data["question"] == data["question"]
    assert [choice["text"] for choice in response_data["choices"]] == data["choices"]


async def test_get_results_not_exists_poll(async_session: AsyncClient) -> None:
    invalid_id = "66ba0f7cd68573b792b449ff"
    response = await async_session.post(f"/getResult/?poll_id={invalid_id}")

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": ExceptionMessages.PollDoesNotExistsException.value}


async def test_get_results_invalid_poll_id(async_session: AsyncClient) -> None:
    invalid_id = "66ba0f7cd68573b792b449"
    response = await async_session.post(f"/getResult/?poll_id={invalid_id}")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": ExceptionMessages.ObjectIdNotValidException.value}
