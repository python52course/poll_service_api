APP_CONTAINER = poll-app
DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file ./app/.env

.PHONY: app app-restart app-down app-logs app-shell tests tests-coverage check-flake8 check-black check-isort fix-black

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

check-flake8:
	${DC} ${ENV} exec ${APP_CONTAINER} flake8 .

check-black:
	${DC} ${ENV} exec ${APP_CONTAINER} black --check .

check-isort:
	${DC} ${ENV} exec ${APP_CONTAINER} isort --check .

fix-black-isort:
	${DC} ${ENV} exec ${APP_CONTAINER} black . ; ${DC} ${ENV} exec ${APP_CONTAINER} isort .
