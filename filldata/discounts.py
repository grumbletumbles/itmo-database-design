import os

from faker import Faker


def fill_discounts(conn):
    cursor = conn.cursor()
    cursor.execute('select * from information_schema.tables where table_name=%s', ('discounts',))
    if cursor.rowcount == 0:
        print('discounts table does not exist')
        return

    fake = Faker()
    discounts_count = int(os.environ['DISCOUNTS_COUNT'])
    discounts = []
    for i in range(discounts_count):
        discounts.append((fake.random_int(min=0, max=100),))

    print('populating discounts...')
    string = 'INSERT INTO discounts (discount) VALUES (%s)'

    print('inserting discounts...')

    cursor.executemany(string, discounts)

    passenger_discounts = []
    for i in range(int(os.environ['PASSENGERS_COUNT'])):
        passenger_discounts.append((i + 1, fake.random_int(min=1, max=discounts_count)))

    string = 'INSERT INTO passengers_discounts (passenger_id, discount_id) VALUES (%s, %s)'
    cursor.executemany(string, passenger_discounts)

    seats_discounts = []
    for i in range(int(os.environ['SEATS_COUNT'])):
        seats_discounts.append((i + 1, fake.random_int(min=1, max=discounts_count)))

    string = 'INSERT INTO seats_discounts (seat_id, discount_id) VALUES (%s, %s)'
    cursor.executemany(string, seats_discounts)

    conn.commit()
    print('discounts inserted successfully')
