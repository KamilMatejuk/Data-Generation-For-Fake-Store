CREATE user user123 identified by password;
grant CREATE SESSION, ALTER SESSION, CREATE DATABASE LINK,
    CREATE MATERIALIZED VIEW, CREATE PROCEDURE, CREATE PUBLIC SYNONYM,
    CREATE ROLE, CREATE SEQUENCE, CREATE SYNONYM, CREATE TABLE,
    CREATE TRIGGER, CREATE TYPE, CREATE VIEW, UNLIMITED TABLESPACE
    to user123;