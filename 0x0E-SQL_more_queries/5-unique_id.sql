-- create a tabke 'unique_id' with two columns 'id' that have a default and unique value of 1 and 'name'
CREATE TABLE IF NOT EXISTS unique_id(
   id INT UNIQUE DEFAULT 1,
   name VARCHAR(256)
);
