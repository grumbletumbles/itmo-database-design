import os
from enum import Enum
import random
from faker import Faker


class Seat(Enum):
    economy = 1
    business = 2
    first = 3


def fill_seats(conn):
    cursor = conn.cursor()
    cursor.execute('select * from information_schema.tables where table_name=%s', ('seats',))
    if cursor.rowcount == 0:
        print('seats table does not exist')
        return

    fake = Faker()
    seats = []
    flights = int(os.environ['FLIGHTS_COUNT'])
    # ids = random.sample(range(1, flights + 1), flights)
    for i in range(int(os.environ['SEATS_COUNT'])):
        seat = (
            # ids[i],
            fake.random_int(min=1, max=flights),
            fake.enum(Seat).name,
            fake.pyint(min_value=1, max_value=100000),
            fake.pybool(),
            fake.pybool(),
        )
        seats.append(seat)

    print('populating seats...')
    string = '''
    INSERT INTO seats (flight_id, class, price, reserved, luggage_included) 
    VALUES (%s, %s, %s, %s, %s)
    '''

    print('inserting seats...')

    cursor.executemany(string, seats)

    conn.commit()
    print('seats inserted successfully')
