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

make app
```

<h2 id="routes">📍 API Endpoints</h2>

list main routes of poll_service_api, and what are their expected request bodies.
​
| route               | description
|----------------------|-----------------------------------------------------
| <kbd>POST /api/createPoll/</kbd>     | Create a vote with multiple answers
| <kbd>POST /api/poll/</kbd>     | to vote for a specific option: <poll_id, choice_id>
| <kbd>POST /api/getResult/</kbd>     | get the result for a specific vote: <poll_id>
