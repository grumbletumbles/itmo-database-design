FROM postgres:latest

COPY migrations/ /migrations/

COPY *.sh /docker-entrypoint-initdb.d/
COPY *.txt /
EXPOSE 5432
