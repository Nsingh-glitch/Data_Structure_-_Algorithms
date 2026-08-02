# Write your MySQL query statement below
select name,bonus from Employee left join Bonus on 
Bonus.empId=Employee.empId where Bonus.bonus<1000 OR Bonus.bonus is NUll;
