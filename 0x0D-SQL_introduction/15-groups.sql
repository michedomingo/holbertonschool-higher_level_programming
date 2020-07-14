-- Lists number of records with same score in second_table of database hbtn_0c_0
-- Displays the score then number of records for score
-- Sorted by number of records (descending)
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score ORDER BY score DESC;
