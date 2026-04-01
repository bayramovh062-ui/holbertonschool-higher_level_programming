-- we can see how much same score in the table with using this sql code
SELECT count(score) FROM second_table
ORDER BY score desc
GROUP By score;
