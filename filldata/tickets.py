import os
import random
from faker import Faker


def fill_tickets(conn):
    cursor = conn.cursor()
    cursor.execute('select * from information_schema.tables where table_name=%s', ('tickets',))
    if cursor.rowcount == 0:
        print('tickets table does not exist')
        return

    fake = Faker()
    tickets = []
    seats_count = int(os.environ['SEATS_COUNT'])
    passengers = int(os.environ['PASSENGERS_COUNT'])
    ids = random.sample(range(1, seats_count + 1), seats_count)
    for i in range(seats_count):
        ticket = (
            fake.random_int(min=1, max=passengers),
            ids[i]
        )
        tickets.append(ticket)

    print('populating tickets...')
    string = '''
    INSERT INTO tickets (passenger_id, seat_id)
    VALUES (%s, %s)
    '''

    print('inserting tickets...')

    cursor.executemany(string, tickets)

    conn.commit()
    print('tickets inserted successfully')
