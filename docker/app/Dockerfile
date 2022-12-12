FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update -y \
    && apt -y update && apt -y upgrade \
    && apt-get install -y build-essential \
    && apt-get install -y libpq-dev gcc \
    && apt-get install -y netcat \
    && apt-get autoremove -y \
    && apt-get autoclean -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

ADD requirements.txt /app/requirements.txt
ADD requirements-ci.txt /app/requirements-ci.txt

RUN python -m ensurepip --upgrade
RUN pip install --upgrade -r /app/requirements.txt
RUN pip install -r /app/requirements-ci.txt

ADD . /app

RUN sed -i 's/\r$//g' /app/docker/entrypoint.sh
RUN chmod +x /app/docker/entrypoint.sh

ENTRYPOINT ["/app/docker/entrypoint.sh"]
