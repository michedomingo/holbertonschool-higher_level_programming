-- Lists all records of the table second_table of the database hbtn_0c_0
-- Displays score then name, listed by descending score
-- Records without without a name will not be displayed
SELECT score, NAME from second_table WHERE name IS NOT NULL
ORDER BY score DESC;
