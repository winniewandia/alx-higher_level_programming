--  lists all records of the table
-- query that  lists all records of the table and does not list rows without a name value
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
