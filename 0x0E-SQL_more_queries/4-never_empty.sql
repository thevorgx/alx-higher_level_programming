-- create a tabke 'id_not_null' with two columns 'id' that have a default value of 1 and 'name'
CREATE TABLE IF NOT EXISTS id_not_null(
   id INT DEFAULT 1,
   name VARCHAR(256)
);
