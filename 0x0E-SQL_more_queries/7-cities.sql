-- create a database named 'hbtn_0d_usa' inside the database create a table 'cities' that have a foreign key(state_id) reference from 'states(id)'
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
    id INT UNIQUE PRIMARY KEY NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id),
    name VARCHAR(256) NOT NULL
);
