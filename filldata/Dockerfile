FROM python:latest

WORKDIR /filldata

ADD . /filldata

RUN wget -O /wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh
RUN chmod +x /wait-for-it.sh

RUN pip install faker
RUN pip install psycopg2
RUN pip install faker_airtravel
