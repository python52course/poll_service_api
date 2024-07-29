APP_CONTAINER = poll-app
DC = docker compose
EXEC = docker exec -it
LOGS = docker logs

.PHONY: app 
app:
	${DC} up --build -d

.PHONY: app-restart
app-restart:
	${DC} restart

.PHONY: app-down
app-down:
	${DC} down

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER}

.PHONY: app-shell
app-shell:
	${EXEC} ${APP_CONTAINER} /bin/bash

.PHONY: tests
tests:
	${EXEC} ${APP_CONTAINER} pytest -vs

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
