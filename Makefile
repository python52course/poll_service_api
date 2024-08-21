APP_CONTAINER = poll-app
DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file ./app/.env

.PHONY: app app-restart app-down app-logs app-shell tests tests-coverage mypy ruff-check ruff-fix

app:
	${DC} ${ENV} up --build -d

app-restart:
	${DC} ${ENV} restart

app-down:
	${DC} ${ENV} down

app-logs:
	${DC} logs -f ${APP_CONTAINER}

app-shell:
	${DC} ${ENV} exec ${APP_CONTAINER} /bin/bash

tests:
	${DC} ${ENV} exec ${APP_CONTAINER} pytest -vs

tests-coverage:
	${DC} ${ENV} exec ${APP_CONTAINER} pytest --cov=. tests

mypy:
	${DC} ${ENV} exec ${APP_CONTAINER} mypy --explicit-package-bases .

ruff-check:
	${DC} ${ENV} exec ${APP_CONTAINER} ruff check .

ruff-fix:
	${DC} ${ENV} exec ${APP_CONTAINER} ruff check . --fix
