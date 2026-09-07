# Write your MySQL query statement below
SELECT
    author_id as id
FROM 
    Views
WHERE
    author_id=viewer_id
Group by 
    author_id
ORDER BY
    author_id ASC;

