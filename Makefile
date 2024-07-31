APP_CONTAINER = poll-app
DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file ./app/.env

.PHONY: app 
app:
	${DC} ${ENV} up --build -d

.PHONY: app-restart
app-restart:
	${DC} ${ENV} restart

.PHONY: app-down
app-down:
	${DC} ${ENV} down

.PHONY: app-logs
app-logs:
	${LOGS} ${ENV} ${APP_CONTAINER}

.PHONY: app-shell
app-shell:
	${EXEC} ${ENV} ${APP_CONTAINER} /bin/bash

.PHONY: tests
tests:
	${EXEC} ${ENV} ${APP_CONTAINER} pytest -vs

.PHONY: tests-coverage
tests-coverage:
	${EXEC} ${ENV} ${APP_CONTAINER} pytest --cov=. tests/

.PHONY: check-flake8
check-flake8:
	${EXEC} ${APP_CONTAINER} flake8 .

.PHONY: check-black
check-black:
	${EXEC} ${APP_CONTAINER} black --check .

.PHONY: check-isort
check-isort:
	${EXEC} ${APP_CONTAINER} isort --check .

.PHONY: fix-black
fix-black-isort:
	${EXEC} ${APP_CONTAINER} black . ; ${EXEC} ${APP_CONTAINER} isort .
