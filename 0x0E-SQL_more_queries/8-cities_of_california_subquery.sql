-- Write a script that lists all the cities of California that can be found in the database
-- Sub queries
SELECT id,  name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = "California"
)
ORDER BY cities.id ASC;
