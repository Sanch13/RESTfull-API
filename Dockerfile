# базовый образ
FROM python:3.11

LABEL authors="sanch"

# not to create files.pyc
ENV PYTHONDONTWRITEBYTECODE=1
# to see an output in real time
ENV PYTHONUNBUFFERED=1

# download dependence
COPY /requirements.txt /temp/requirements.txt
# copy our app
COPY api /api
# sign workdir
WORKDIR /api
# install all dependence
RUN pip install -r /temp/requirements.txt

RUN adduser --disabled-password sanch

USER sanch

EXPOSE 8000
