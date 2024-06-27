-- Displays the average temperature (in Fahrenheit) by city orderd by descending temperature.
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;
