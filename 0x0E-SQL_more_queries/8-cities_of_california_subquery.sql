-- query asking the database to find and print the 'id' and 'name' of all cities that belong to the state of 'California' and sorting them by cities 'id'
SELECT cities.id, cities.name FROM cities
WHERE cities.state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id ASC;
