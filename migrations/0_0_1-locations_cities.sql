CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    country VARCHAR(255) NOT NULL,
    offset_from_utc INTERVAL NOT NULL
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location_id INTEGER NOT NULL REFERENCES locations(id)
);