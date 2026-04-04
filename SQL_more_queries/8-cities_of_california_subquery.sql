-- this code gives us an examle about subquery

SELECT id, name FROM cities
WHERE id = (
	SELECT state_id FROM states
	WHERE name = 'california'
)
ORDER BY id;
