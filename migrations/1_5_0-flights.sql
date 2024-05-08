CREATE TABLE IF NOT EXISTS flights (
    id SERIAL PRIMARY KEY,
    from_airport_id INTEGER NOT NULL REFERENCES airports(id),
    to_airport_id INTEGER NOT NULL REFERENCES airports(id),
    departure_time TIME NOT NULL,
    arrival_time TIME NOT NULL,
    airline_id INTEGER NOT NULL references airlines(id),
    plane_id INTEGER NOT NULL references planes(id),
    luggage_price BIGINT NOT NULL
);