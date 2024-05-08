CREATE TYPE seat_class AS ENUM ('economy', 'business', 'first');

CREATE TABLE IF NOT EXISTS seats (
    id SERIAL PRIMARY KEY,
    flight_id INTEGER NOT NULL REFERENCES flights(id),
    class seat_class NOT NULL,
    price DECIMAL NOT NULL,
    reserved BOOLEAN NOT NULL,
    luggage_included BOOLEAN NOT NULL
);