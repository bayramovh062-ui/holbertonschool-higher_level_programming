-- we can see how much same score in the table with using this sql code
SELECT score, count(score) FROM second_table
GROUP BY score
ORDER BY score DESC;

