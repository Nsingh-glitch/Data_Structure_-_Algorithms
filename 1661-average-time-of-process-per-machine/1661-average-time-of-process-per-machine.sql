# Write your MySQL query statement below
WITH process_time AS(
    select 
        a.machine_id,
        b.timestamp-a.timestamp as duration
    from Activity a
    JOIN Activity b
        on a.machine_id=b.machine_id
        AND a.process_id=b.process_id
        WHERE a.activity_type = 'start'
        AND b.activity_type = 'end'
)

select 
    machine_id,
    ROUND(AVG(duration),3) AS processing_time

from process_time
group by machine_id;