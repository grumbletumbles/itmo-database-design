CREATE TABLE IF NOT EXISTS locations (
    id SERIAL PRIMARY KEY,
    country VARCHAR(255) NOT NULL,
    offset_from_utc INTERVAL NOT NULL
);
