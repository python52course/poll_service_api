APP_CONTAINER = poll-app
DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file ./app/.env

.PHONY: app app-restart app-down app-logs app-shell tests tests-coverage check-flake8 check-black check-isort fix-black

app:
	${DC} ${ENV} up --build -d

.PHONY: app-restart
app-restart:
	${DC} ${ENV} restart

app-down:
	${DC} ${ENV} down

app-logs:
	${LOGS} ${APP_CONTAINER}

app-shell:
	${EXEC} ${ENV} ${APP_CONTAINER} /bin/bash

tests:
	${EXEC} ${ENV} ${APP_CONTAINER} pytest -vs

tests-coverage:
	${EXEC} ${ENV} ${APP_CONTAINER} pytest --cov=. tests/

check-flake8:
	${EXEC} ${APP_CONTAINER} flake8 .

check-black:
	${EXEC} ${APP_CONTAINER} black --check .

check-isort:
	${EXEC} ${APP_CONTAINER} isort --check .

fix-black-isort:
	${EXEC} ${APP_CONTAINER} black . ; ${EXEC} ${APP_CONTAINER} isort .
