-- this code creates a new database and table and gives constraints in this table id state id name columns

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(id INT PRIMARY KEY AUTO_INCREMENT, state_id INT, FOREIGN KEY(state_id) REFERENCES states(state_id, name VARCHAR(256) NOT NULL))
