CREATE TABLE discounts (
    id SERIAL PRIMARY KEY,
    discount DECIMAL NOT NULL
);

CREATE TABLE passengers_discounts (
    passenger_id INTEGER REFERENCES passengers(id),
    discount_id INTEGER REFERENCES discounts(id)
);

CREATE TABLE seats_discounts (
    seat_id INTEGER REFERENCES seats(id),
    discount_id INTEGER REFERENCES discounts(id)
);