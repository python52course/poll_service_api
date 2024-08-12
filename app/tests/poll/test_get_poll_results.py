import pytest


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
async def test_get_results_exists_poll(async_session, create_poll_fixture):
    data = create_poll_fixture[1]
    poll_id = create_poll_fixture[0]["id"]
    response = await async_session.get(f"/getResult/{poll_id}/")
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["id"] == poll_id
    assert response_data["question"] == data["question"]
    assert [choice["text"] for choice in response_data["choices"]] == data["choices"]


async def test_get_results_not_exists_poll(async_session):
    invalid_id = "66ba0f7cd68573b792b449ff"
    response = await async_session.get(f"/getResult/{invalid_id}/")

    assert response.status_code == 404
    assert response.json() == {"detail": "The poll not found"}


async def test_get_results_invalid_poll_id(async_session):
    invalid_id = "66ba0f7cd68573b792b449"
    response = await async_session.get(f"/getResult/{invalid_id}/")

    assert response.status_code == 400
    assert response.json() == {"detail": "poll_id is not valid, poll_id must be 24 character"}
