-- 176. 第二高的薪水
-- SQL架构
-- 编写一个 SQL 查询，获取 Employee 表中第二高的薪水（Salary） 。
--
-- +----+--------+
-- | Id | Salary |
-- +----+--------+
-- | 1  | 100    |
-- | 2  | 200    |
-- | 3  | 300    |
-- +----+--------+
-- 例如上述 Employee 表，SQL查询应该返回 200 作为第二高的薪水。如果不存在第二高的薪水，那么查询应返回 null。
--
-- +---------------------+
-- | SecondHighestSalary |
-- +---------------------+
-- | 200                 |
-- +---------------------+


-- 方式1 当为空时会不返回东西，根据要求需要返回null(所以本方法不满足要求)
select distinct Salary as SecondHighestSalary from Employee
order by Salary desc
limit 1  offset 1 -- offset 需要写在limit 后面
-- 子查询处理null的问题
select (select distinct Salary as SecondHighestSalary from Employee
order by Salary desc
limit 1  offset 1
) as SecondHighestSalary


-- 方式2
select ifnull( -- 如果第一个参数为空，则返回第二个参数
(select distinct Salary from Employee
order by Salary desc
limit 1  offset 1),null
) as SecondHighestSalary