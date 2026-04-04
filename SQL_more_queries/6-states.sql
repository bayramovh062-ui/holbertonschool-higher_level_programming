-- this code creates new database and table in this table id should be primary key and auto_generated and name not null

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(256) NOT NULL);
