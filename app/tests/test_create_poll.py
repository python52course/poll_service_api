from httpx import AsyncClient, request

from main import app



async def test_create_poll(connection_db):
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000/api") as ac:
        data = {
            "question": "Какой ваш любимый покемон?",
            "choices": ["Пикачу", "Чармандер", "Сквиртл"],
        }
        response = await ac.post("/createPoll/", json=data)
        assert response.status_code == 200



async def test_create_existing_poll(connection_db):
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000/api") as ac:
        data = {
            "question": "Какой ваш любимый покемон?",
            "choices": ["Пикачу", "Чармандер", "Сквиртл"],
        }
        response = await ac.post("/createPoll/", json=data)
        assert response.status_code == 200



### THIS IS WORK BUT IT IS WRITING TO MAIN DATABASE
# def test_create_poll(connection_db):
#     data = {
#             "question": "Какой ваш любимый покемон?",
#             "choices": ["Пикачу", "Чармандер", "Сквиртл"],
#         }
#     response = request('POST', 'http://127.0.0.1:8000/api/createPoll/', json=data)
#     assert response.status_code == 200


# def test_create_existing_poll(connection_db):
#     data = {
#             "question": "Какой ваш любимый покемон?",
#             "choices": ["Пикачу", "Чармандер", "Сквиртл"],
#         }
#     response = request('POST', 'http://127.0.0.1:8000/api/createPoll/', json=data)

#     assert response.status_code == 200
