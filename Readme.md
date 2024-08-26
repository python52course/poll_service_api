# This project is a simple voting service built with FastAPI.

## Technologies

- Python
- FastAPI
- MongoDB
- Docker
- Docker-Compose

## Getting started

###  list requirements necessary for running project.

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)


### Cloning

```bash
git clone https://github.com/python52course/poll_service_api
```

### Config .env variables

Use the `.env.example` as reference to create your configuration file `.env`

### Starting

How to start

```bash
cd poll_service_api

docker compose up

docker compose exec poll-app pytest --cov=. tests
```

## API Endpoints

list routes of poll_service_api, and what are their expected request bodies.
​
| route               | description
|----------------------|-----------------------------------------------------
| <kbd>POST /api/createPoll/</kbd>     | Create a vote with multiple answers
| <kbd>POST /api/getResult/</kbd>     | get the result for a specific vote: <poll_id>
| <kbd>POST /api/poll/</kbd>     | to vote for a specific option: <poll_id, choice_id>

## POST /api/createPoll/

**REQUEST**
```bash
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


## POST /api/getResult/

**REQUEST**
```bash
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

## POST /api/poll/

**REQUEST**
```bash
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
