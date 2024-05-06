import os

from faker import Faker


def fill_locations(conn):
    cursor = conn.cursor()
    cursor.execute('select * from information_schema.tables where table_name=%s', ('locations',))
    if cursor.rowcount == 0:
        print('locations table does not exist')
        return

    fake = Faker()
    locations = []
    for i in range(int(os.environ['LOCATIONS_COUNT'])):
        loc = (fake.country(), fake.time(pattern='%H:%M:%S'))
        locations.append(loc)

    print('populating locations...')
    string = 'INSERT INTO locations (country, offset_from_utc) VALUES (%s, %s)'

    print('inserting locations...')

    cursor.executemany(string, locations)

    conn.commit()
    print('locations inserted successfully')
