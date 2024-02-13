-- echo score and name columns from the table 'second_table' on rows where core >= 10 in descending order
SELECT score, name FROM second_table
WHERE score >= 10 ORDER BY score DESC;
