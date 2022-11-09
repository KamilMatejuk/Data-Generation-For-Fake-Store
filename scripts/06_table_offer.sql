CREATE TABLE Offer (
    offer_id NUMBER,
    name CHAR(300) CONSTRAINT offer_name_not_null NOT NULL,
    description VARCHAR(2000) CONSTRAINT offer_description_not_null NOT NULL,
    price NUMBER CONSTRAINT offer_price_not_null NOT NULL,
    offer_date DATE CONSTRAINT offer_offer_date_not_null NOT NULL,
    quantity NUMBER CONSTRAINT offer_quantity_not_null NOT NULL,
    fk_customer NUMBER CONSTRAINT offer_fk_customer_not_null NOT NULL,
    fk_category NUMBER CONSTRAINT offer_fk_category_not_null NOT NULL,
    CONSTRAINT offer_pk PRIMARY KEY (offer_id)
);
