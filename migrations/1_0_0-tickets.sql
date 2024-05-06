CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    passenger_id INTEGER REFERENCES passengers(id),
    seat_id INTEGER REFERENCES seats(id)
);