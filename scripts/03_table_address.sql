CREATE TABLE Address (
    address_id NUMBER,
    country CHAR(60) CONSTRAINT address_country_not_null NOT NULL,
    city CHAR(100) CONSTRAINT address_city_not_null NOT NULL,
    state CHAR(300) CONSTRAINT address_state_not_null NOT NULL,
    street CHAR(300) CONSTRAINT address_street_not_null NOT NULL,
    street_number NUMBER CONSTRAINT address_street_number_not_null NOT NULL,
    apartment_number NUMBER,
    postal_code CHAR(20) CONSTRAINT address_postal_code_not_null NOT NULL,
    fk_customer NUMBER CONSTRAINT address_fk_customer_not_null NOT NULL,
    CONSTRAINT address_pk PRIMARY KEY (address_id)
);
