CREATE TABLE Delivery (
    delivery_id NUMBER,
    expected_arrival DATE,
    delivery_type CHAR(100) CONSTRAINT delivery_delivery_type_not_null NOT NULL,
    status CHAR(100) CONSTRAINT delivery_status_not_null NOT NULL,
    sent_date DATE,
    fk_address NUMBER CONSTRAINT delivery_fk_address_not_null NOT NULL,
    fk_purchase NUMBER CONSTRAINT delivery_fk_purchase_not_null NOT NULL,
    CONSTRAINT delivery_pk PRIMARY KEY (delivery_id)
);
