-- this code create a new table and id should be unique and its default value should be 1 in this table

CREATE TABLE IF NOT EXISTS unique_id(id INT UNIQUE DEFAULT 1, name VARCHAR(256));
