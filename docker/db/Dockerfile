FROM postgres:15.1

RUN mkdir -p /tmp/psql_data/

COPY dumps/last_dump.db /tmp/psql_data/
COPY docker/init_docker_postgres.sh /docker-entrypoint-initdb.d/
