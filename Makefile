APP_CONTAINER = poll-app
DC = docker compose
EXEC = docker exec -it
LOGS = docker logs

.PHONY: app app-restart app-down app-logs app-shell tests tests-coverage mypy ruff-check ruff-fix

app:
	${DC} up --build -d

app-restart:
	${DC} restart

app-down:
	${DC} down

app-logs:
	${DC} logs -f ${APP_CONTAINER}

app-shell:
	${DC} exec ${APP_CONTAINER} /bin/bash

tests:
	${DC} exec ${APP_CONTAINER} pytest -vs

tests-coverage:
	${DC} exec ${APP_CONTAINER} pytest --cov=. tests

mypy:
	${DC} exec -T ${APP_CONTAINER} mypy --explicit-package-bases .

ruff-check:
	${DC} exec -T ${APP_CONTAINER} ruff check .

ruff-fix:
	${DC} exec -T ${APP_CONTAINER} ruff check . --fix
