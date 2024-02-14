-- test
SELECT city, AVG(temperatures) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
