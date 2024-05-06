CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL,
    passport VARCHAR(10) NOT NULL,
    flight_xp BIGINT NOT NULL
);