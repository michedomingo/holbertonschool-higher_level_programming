-- Lists all records with a score >= 10 in the table second_table of hbtn_0c_0
-- Results should display both the score then name, ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
