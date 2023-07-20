FROM python:3.11.4-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app/

COPY ./app /app/

COPY requirements.txt requirements.txt

# RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r requirements.txt
