# Poll Service

## Project Description
This project implements a poll service.  You can create a poll with multiple answers, vote for a specific options, and get the result for a specific poll.

## Tech Stack
- Python
- FastAPI
- MongoDB
- Docker
- Docker-Compose

## Installation

### Clone the project
```bash
   git clone https://github.com/python52course/poll_service_api
```
### Go to the project directory
```bash
  cd my-project
```

### Config .env variables
Use the `.env.example` as reference to create your configuration file `.env`

### Run in Docker
```bash
docker compose up
```

### Running Tests
To run tests, run the following command
```bash
docker compose exec poll-app pytest --cov=. tests
```

## API Reference

#### list routes of poll_service_api, and what are their expected request bodies.

| Route                       | Description
|-----------------------------|-----------------------------------------------------
| `POST` /api/createPoll/     | Create a vote with multiple answers
| `POST` /api/getResult/      | get the result for a specific vote: <poll_id>
| `POST` /api/poll/           | to vote for a specific option: <poll_id, choice_id>

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

**Example Response:**
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

**Example RESPONSE**
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

**Example RESPONSE**
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
