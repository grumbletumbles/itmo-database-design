#!/bin/bash

POSTGRES_DB=$DB_NAME
POSTGRES_USER=$DB_USER

#users=("user1" "user2" "user3")

psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" 


psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "CREATE ROLE reader;"
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "CREATE ROLE writer;"
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "CREATE ROLE group_role WITH NOLOGIN;"


psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "GRANT SELECT ON ALL TABLES IN SCHEMA public TO reader;"
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO writer;"
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO group_role;"

psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "CREATE USER analytic;"

#query=$(cat /analyticscript.txt)
#psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "$query"
psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "GRANT SELECT ON TABLE public.locations TO analytic;"

users="$USERS"
IFS=";"
read -ra arrusers <<< "$users"

for user in "${arrusers[@]}"; do
    psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "CREATE USER $user;"
    psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "GRANT group_role TO $user;"
done
