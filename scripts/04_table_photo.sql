CREATE TABLE Photo (
    photo_id NUMBER,
    name CHAR(100) CONSTRAINT photo_name_not_null NOT NULL,
    file_name CHAR(200) CONSTRAINT photo_file_name_not_null NOT NULL,
    upload_date DATE CONSTRAINT photo_upload_date_not_null NOT NULL,
    file_extension CHAR(10) CONSTRAINT photo_file_extension_not_null NOT NULL,
    fk_offer NUMBER CONSTRAINT photo_fk_offer_not_null NOT NULL,
    CONSTRAINT photo_pk PRIMARY KEY (photo_id)
);
