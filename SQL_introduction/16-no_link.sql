-- we can see score and name coumns and all rows with using this code but where name is not null
SELECT score, name FROM second_table
WHERE score IS NOT NULL
ORDER BY score DESC;
