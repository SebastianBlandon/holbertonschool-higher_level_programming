-- script that lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server. 
-- SQL introduction project
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city ORDER BY avg_temp DESC;
