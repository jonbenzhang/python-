-- 184. 部门工资最高的员工
-- SQL架构
-- Employee 表包含所有员工信息，每个员工有其对应的 Id, salary 和 department Id。
--
-- +----+-------+--------+--------------+
-- | Id | Name  | Salary | DepartmentId |
-- +----+-------+--------+--------------+
-- | 1  | Joe   | 70000  | 1            |
-- | 2  | Jim   | 90000  | 1            |
-- | 3  | Henry | 80000  | 2            |
-- | 4  | Sam   | 60000  | 2            |
-- | 5  | Max   | 90000  | 1            |
-- +----+-------+--------+--------------+
-- Department 表包含公司所有部门的信息。
--
-- +----+----------+
-- | Id | Name     |
-- +----+----------+
-- | 1  | IT       |
-- | 2  | Sales    |
-- +----+----------+
-- 编写一个 SQL 查询，找出每个部门工资最高的员工。对于上述表，您的 SQL 查询应返回以下行（行的顺序无关紧要）。
--
-- +------------+----------+--------+
-- | Department | Employee | Salary |
-- +------------+----------+--------+
-- | IT         | Max      | 90000  |
-- | IT         | Jim      | 90000  |
-- | Sales      | Henry    | 80000  |
-- +------------+----------+--------+
-- 解释：
--
-- Max 和 Jim 在 IT 部门的工资都是最高的，Henry 在销售部的工资最高。
-- 方式1 滑动窗口
select a.Name as Department, t.Name as Employee,t.Salary as Salary from
(select *, rank() over(partition by DepartmentId order by Salary desc) as rk from Employee) t , Department a
where t.rk=1 and t.DepartmentId=a.Id
-- 方式2 group by, 效率高
select b.Name as Department, a.Name as Employee,a.Salary as Salary from Employee a, Department b
where a.DepartmentId=b.Id and  (a.DepartmentId,a.Salary) in  (select DepartmentId, max(Salary) from  Employee group by DepartmentId)
