import os

from faker import Faker
from faker_airtravel import AirTravelProvider


def fill_airlines(conn):
    cursor = conn.cursor()
    cursor.execute('select * from information_schema.tables where table_name=%s', ('airlines',))
    if cursor.rowcount == 0:
        print('airlines table does not exist')
        return

    fake = Faker()
    fake.add_provider(AirTravelProvider)
    airlines = []
    for i in range(int(os.environ['AIRLINES_COUNT'])):
        try:
            airline = fake.unique.airline()
        except Exception as e:
            break
        airlines.append((airline,))

    print('populating airlines...')
    string = 'INSERT INTO airlines (name) VALUES (%s)'

    print('inserting airlines...')

    cursor.executemany(string, airlines)

    conn.commit()
    print('airlines inserted successfully')
