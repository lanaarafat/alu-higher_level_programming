-- lists all cities in the database
SELECT cities.id, cities.name, states.name FROM cities AS c INNER JOIN states AS s ON c.state_id = states.id ORDER BY c.id;
