-- this code gives us an examle about subquery

SELECT state_id, name FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name = 'california'
)
ORDER BY id;
