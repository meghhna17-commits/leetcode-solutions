# Write your MySQL query statement below
select e.name as EMPLOYEE from Employee e JOIN Employee m on e.managerID=m.id where e.salary > m.salary;