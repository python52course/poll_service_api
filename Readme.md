# This project is a simple voting service built with FastAPI.
![Tests](https://github.com/python52course/poll_service_api/actions/workflows/ci.yml/badge.svg)

<h2 id="technologies">Technologies</h2>

- Python
- FastAPI
- MongoDB
- Docker
- Docker-Compose

<h2 id="started"> Getting started</h2>

###  list all requirements necessary for running project.

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)


<h3>Cloning</h3>

```bash
git clone https://github.com/python52course/poll_service_api
```

<h3>Config .env variables</h2>

Use the `.env.example` as reference to create your configuration file `.env`

<h3>Starting</h3>

How to start

```bash
cd poll_service_api

docker compose --env-file ./app/.env up --build -d
```

<h2 id="routes">📍 API Endpoints</h2>

list main routes of poll_service_api, and what are their expected request bodies.
​
| route               | description
|----------------------|-----------------------------------------------------
| <kbd>POST /api/createPoll/</kbd>     | Create a vote with multiple answers
| <kbd>POST /api/getResult/</kbd>     | get the result for a specific vote: <poll_id>
| <kbd>POST /api/poll/</kbd>     | to vote for a specific option: <poll_id, choice_id>

<h2 id="post-auth-detail">POST /api/createPoll/</h2>

**REQUEST**
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/api/createPoll/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "choices": [
    "Pikachu",
    "Charmander",
    "Squirting"
  ],
  "question": "What is your favorite Pokemon?"
}'
```

**RESPONSE**
```json
{
  "id": "66c748e3357217ad1223bf98",
  "question": "What is your favorite Pokemon?",
  "choices": [
    {
      "id": "048d83",
      "text": "Pikachu",
      "votes": 0
    },
    {
      "id": "4a2fd7",
      "text": "Charmander",
      "votes": 0
    },
    {
      "id": "59d97a",
      "text": "Squirting",
      "votes": 0
    }
  ]
}
```


<h2 id="post-auth-detail">POST /api/getResult/</h2>

**REQUEST**
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/api/getResult/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "poll_id": "66c748e3357217ad1223bf98"
}'
```

**RESPONSE**
```json
{
  "id": "66c748e3357217ad1223bf98",
  "question": "What is your favorite Pokemon?",
  "choices": [
    {
      "id": "048d83",
      "text": "Pikachu",
      "votes": 0
    },
    {
      "id": "4a2fd7",
      "text": "Charmander",
      "votes": 0
    },
    {
      "id": "59d97a",
      "text": "Squirting",
      "votes": 0
    }
  ]
}
```

<h2 id="post-auth-detail">POST /api/poll/</h2>

**REQUEST**
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/api/poll/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "poll_id": "66ba0f7cd68573b792b449ff",
  "choice_id": "106d56"
}'
```

**RESPONSE**
```json
{
  "id": "66c748e3357217ad1223bf98",
  "question": "What is your favorite Pokemon?",
  "choices": [
    {
      "id": "048d83",
      "text": "Pikachu",
      "votes": 1
    },
    {
      "id": "4a2fd7",
      "text": "Charmander",
      "votes": 0
    },
    {
      "id": "59d97a",
      "text": "Squirting",
      "votes": 0
    }
  ]
}
```
