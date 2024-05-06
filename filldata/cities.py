import os

from faker import Faker


def fill_cities(conn):
    cursor = conn.cursor()
    cursor.execute('select * from information_schema.tables where table_name=%s', ('cities',))
    if cursor.rowcount == 0:
        print('cities table does not exist')
        return

    fake = Faker()
    cities = []
    for i in range(int(os.environ['CITIES_COUNT'])):
        city = (fake.city(), fake.pyint(min_value=1, max_value=int(os.environ['LOCATIONS_COUNT'])))
        cities.append(city)

    print('populating cities...')
    string = 'INSERT INTO cities (name, location_id) VALUES (%s, %s)'

    print('inserting cities...')

    cursor.executemany(string, cities)

    conn.commit()
    print('cities inserted successfully')
