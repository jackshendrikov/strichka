#!/bin/bash

DATABASE_NAME=${POSTGRES_DB}
DB_DUMP_LOCATION="/tmp/psql_data/last_dump.db"

echo "*** CREATING DATABASE ***"

# create default database
gosu postgres postgres --single <<EOSQL
  CREATE DATABASE "$DATABASE_NAME";
  ALTER USER postgres CREATEDB;
  GRANT ALL PRIVILEGES ON DATABASE "$DATABASE_NAME" TO postgres;
EOSQL

if [ "$POPULATE_LOCAL_DB" = true ]; then
  psql "$DATABASE_NAME" < "$DB_DUMP_LOCATION"
  echo "*** DUMP CREATED! ***"
fi

echo "*** DATABASE CREATED! ***"
