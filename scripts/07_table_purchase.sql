CREATE TABLE Purchase (
    purchase_id NUMBER,
    quantity NUMBER CONSTRAINT purchase_quantity_not_null NOT NULL,
    additional_info VARCHAR(1000),
    rating NUMBER,
    purchase_date DATE CONSTRAINT purchase_purchase_date_not_null NOT NULL,
    fk_offer NUMBER CONSTRAINT purchase_fk_offer_not_null NOT NULL,
    fk_customer NUMBER CONSTRAINT purchase_fk_customer_not_null NOT NULL,
    CONSTRAINT purchase_pk PRIMARY KEY (purchase_id)
);
