-- Lists all records of the table second_table where the name column is not null
SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;