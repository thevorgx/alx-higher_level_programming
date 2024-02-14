-- display score and name columns from 'second_table' wehere rows with NULL and empty name won't show and order in descending order
SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
