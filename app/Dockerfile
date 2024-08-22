FROM python:3.8.19

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install poetry

ADD pyproject.toml /app

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi
