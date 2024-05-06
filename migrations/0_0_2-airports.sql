CREATE TABLE airports (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    city_id INTEGER NOT NULL REFERENCES cities(id)
);