CREATE TABLE Category (
    category_id NUMBER,
    name CHAR(200) CONSTRAINT category_name_not_null NOT NULL,
    description VARCHAR(1000) CONSTRAINT category_description_not_null NOT NULL,
    fk_category NUMBER,
    CONSTRAINT category_pk PRIMARY KEY (category_id)
);
