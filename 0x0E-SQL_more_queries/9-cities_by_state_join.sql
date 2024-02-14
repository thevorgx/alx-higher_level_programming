-- retrieves data from the 'cities' and 'states' tables using an inner join and orders the results by the 'id 'column of the 'cities' table in ascending order
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
