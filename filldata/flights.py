import os

from faker import Faker


def fill_flights(conn):
    cursor = conn.cursor()
    cursor.execute('select * from information_schema.tables where table_name=%s', ('flights',))
    if cursor.rowcount == 0:
        print('flights table does not exist')
        return

    cursor.execute('select count(*) from airlines')
    airlines = int(cursor.fetchone()[0])

    fake = Faker()
    flights = []
    for i in range(int(os.environ['FLIGHTS_COUNT'])):
        flight = (
            fake.pyint(min_value=1, max_value=int(os.environ['AIRPORTS_COUNT'])),
            fake.pyint(min_value=1, max_value=int(os.environ['AIRPORTS_COUNT'])),
            fake.time(pattern='%Y-%m-%d %H:%M:%S'),
            fake.time(pattern='%Y-%m-%d %H:%M:%S'),
            fake.pyint(min_value=1, max_value=airlines),
            fake.pyint(min_value=1, max_value=int(os.environ['PLANES_COUNT'])),
            fake.pyint(min_value=1, max_value=10000),
        )
        flights.append(flight)

    print('populating flights...')
    string = '''
    INSERT INTO flights (from_airport_id, to_airport_id, departure_time, arrival_time, airline_id, plane_id, luggage_price) 
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''

    print('inserting flights...')

    cursor.executemany(string, flights)

    conn.commit()
    print('flights inserted successfully')
