import psycopg2

from cities import *
from locations import *
from airports import *
from planes import *
from airlines import *
from flights import *
from seats import *
from passengers import *
from discounts import *
from tickets import *

fake = Faker()

print('connecting to database...')
conn = psycopg2.connect(dbname=os.environ['DB_NAME'], user=os.environ['DB_USER'], password=os.environ['DB_PASSWORD'],
                        host='database', port=5432)

# conn = psycopg2.connect(dbname='aviasales', user='postgres', password='admin',
#                         host='database', port=5432)
print('connection successful, generating fake data...')

fill_locations(conn)
fill_cities(conn)
fill_airports(conn)
fill_planes(conn)
fill_airlines(conn)
fill_flights(conn)
fill_seats(conn)
fill_passengers(conn)
fill_discounts(conn)
fill_tickets(conn)

print('done')

conn.close()
