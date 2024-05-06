import os

from faker import Faker


def fill_passengers(conn):
    cursor = conn.cursor()
    cursor.execute('select * from information_schema.tables where table_name=%s', ('passengers',))
    if cursor.rowcount == 0:
        print('passengers table does not exist')
        return

    fake = Faker()
    passengers = []
    for i in range(int(os.environ['PASSENGERS_COUNT'])):
        passport = ''
        for _ in range(10):
            passport += str(fake.random_digit())

        passenger = (
            fake.first_name(),
            fake.last_name(),
            passport,
            fake.random_int(min=0, max=100000)
        )
        passengers.append(passenger)

    print('populating passengers...')
    string = 'INSERT INTO passengers (name, surname, passport, flight_xp) VALUES (%s, %s, %s, %s)'

    print('inserting passengers...')

    cursor.executemany(string, passengers)

    conn.commit()
    print('passengers inserted successfully')
