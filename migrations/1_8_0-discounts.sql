CREATE TABLE IF NOT EXISTS discounts (
    id SERIAL PRIMARY KEY,
    discount DECIMAL NOT NULL
);

CREATE TABLE IF NOT EXISTS passengers_discounts (
    passenger_id INTEGER REFERENCES passengers(id),
    discount_id INTEGER REFERENCES discounts(id),
    PRIMARY KEY (passenger_id, discount_id)
);

CREATE TABLE IF NOT EXISTS seats_discounts (
    seat_id INTEGER REFERENCES seats(id),
    discount_id INTEGER REFERENCES discounts(id),
    PRIMARY KEY (seat_id, discount_id)
);