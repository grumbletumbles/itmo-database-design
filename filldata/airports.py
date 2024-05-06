import os

from faker import Faker
from faker_airtravel import AirTravelProvider


def fill_airports(conn):
    cursor = conn.cursor()
    cursor.execute('select * from information_schema.tables where table_name=%s', ('airports',))
    if cursor.rowcount == 0:
        print('airports table does not exist')
        return

    fake = Faker()
    fake.add_provider(AirTravelProvider)
    airports = []
    for i in range(int(os.environ['AIRPORTS_COUNT'])):
        airport = (fake.airport_name(), fake.pyint(min_value=1, max_value=int(os.environ['CITIES_COUNT'])))
        airports.append(airport)

    print('populating airports...')
    string = 'INSERT INTO airports (name, city_id) VALUES (%s, %s)'

    print('inserting airports...')

    cursor.executemany(string, airports)

    conn.commit()
    print('airports inserted successfully')
