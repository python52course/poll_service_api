FROM python:3.8.19-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt update -y && \
    apt install -y curl

RUN pip install --upgrade pip

COPY ./requirements.txt .
COPY ./requirements-dev.txt .

RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . .
