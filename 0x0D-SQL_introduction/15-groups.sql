-- show the number of folks with a given score in a descending
SELECT score, COUNT(score) AS number FROM second_table
GROUP BY score
ORDER BY number DESC;
