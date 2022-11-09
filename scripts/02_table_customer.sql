CREATE TABLE Customer (
    customer_id NUMBER,
    mail CHAR(40) CONSTRAINT customer_mail_not_null NOT NULL,
    name CHAR(30) CONSTRAINT customer_name_not_null NOT NULL,
    surname CHAR(30) CONSTRAINT customer_surname_not_null NOT NULL,
    date_of_birth DATE CONSTRAINT customer_date_of_birth_not_null NOT NULL,
    description VARCHAR(2000),
    CONSTRAINT customer_pk PRIMARY KEY (customer_id)
);
