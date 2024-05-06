import os

from faker import Faker


def fill_planes(conn):
    cursor = conn.cursor()
    cursor.execute('select * from information_schema.tables where table_name=%s', ('planes',))
    if cursor.rowcount == 0:
        print('planes table does not exist')
        return

    fake = Faker()
    planes = []
    for i in range(int(os.environ['PLANES_COUNT'])):
        plane = (fake.name() + ' plane', 'model ' + fake.name(), fake.pyint(min_value=1, max_value=1000))
        planes.append(plane)

    print('populating planes...')
    string = 'INSERT INTO planes (name, model, capacity) VALUES (%s, %s, %s)'

    print('inserting planes...')

    cursor.executemany(string, planes)

    conn.commit()
    print('planes inserted successfully')
