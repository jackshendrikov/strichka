#!/bin/sh

if [ "$POSTGRES_DB" = "strichka_local" ]; then
  echo "Waiting for postgres..."

  while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
    sleep 0.1
  done

  echo "PostgreSQL started"
fi

make migrate
make runserver_dev

exec "$@"
