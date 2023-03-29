-- display the top 3 city temperaturess
SELECT city, AVG(value)  FROM temperatures WHERE months = 7 OR months = 8 GROUP BY city ORDER BY temperature DESC;
