-- Displays the average temperature (Fahrenheit) by city
-- Ordered by temperature (descending)
SELECT city, AVG(value) as avg_temp FROM temperatures
GOUP BY city ORDER BY avg_temp DESC;
