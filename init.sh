#!/bin/bash

migration="$MIGRATION"

if [ -z "$migration" ]; 
then
  # apply all migrations
  for file in $(ls /migrations/ | sort -t '-')
  do
    psql -d "$DB_NAME" -U "$DB_USER" -f "/migrations/$file"
  done 
else
  version=${migration//"."/"_"}
  for file in $(ls /migrations/ | sort -t '-')
  do
    file_version=$(echo "$file" | grep -Eo "[0-9]+_[0-9]+_[0-9]+")
    if [[ "$file_version" < "$version" ]] || [[ "$file_version" = "$version" ]]; 
    then
      psql -d "$DB_NAME" -U "$DB_USER" -f "/migrations/$file"
    fi 
  done 
fi


