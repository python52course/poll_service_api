from random import choice

import pytest
from fastapi import status


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
async def test_valid_vote(async_session, create_poll_fixture):
    poll_id = create_poll_fixture[0]["id"]
    response = await async_session.get(f"/getResult/{poll_id}/")

    choice_ids = [choice["id"] for choice in response.json()["choices"]]
    choice_id = choice(choice_ids)
    response = await async_session.post(f"/poll/?poll_id={poll_id}&choice_id={choice_id}")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["choices"][choice_ids.index(choice_id)]["votes"] == 1


@pytest.mark.parametrize(
    "poll_id, choice_id, expected_message, status_code",
    [
        (
            "66bf3d2525228d2fb65e0a5b",
            "7f28b0",
            {"detail": "The poll was not found"},
            status.HTTP_404_NOT_FOUND,
        ),
        (
            "66bf3d2525228d2fb65e0",
            "7f28b0",
            {"detail": "poll_id is not valid, poll_id must be 24 character"},
            status.HTTP_400_BAD_REQUEST,
        ),
        (
            "",
            "",
            {"detail": "poll_id is not valid, poll_id must be 24 character"},
            status.HTTP_400_BAD_REQUEST,
        ),
    ],
)
async def test_vote_with_invalid_poll_id(
    async_session, poll_id, choice_id, expected_message, status_code
):
    response = await async_session.post(f"/poll/?poll_id={poll_id}&choice_id={choice_id}")

    assert response.status_code == status_code
    assert response.json() == expected_message


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
async def test_vote_with_invalid_choice_id(async_session, create_poll_fixture):
    poll_id = create_poll_fixture[0]["id"]
    response = await async_session.get(f"/getResult/{poll_id}/")
    choice_id = "7f28b0"
    response = await async_session.post(f"/poll/?poll_id={poll_id}&choice_id={choice_id}")

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == {"detail": "There is no such answer option"}
