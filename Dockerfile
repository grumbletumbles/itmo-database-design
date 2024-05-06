FROM postgres:latest

COPY migrations/ /migrations/

COPY *.sh /docker-entrypoint-initdb.d/

EXPOSE 5432
