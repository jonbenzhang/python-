-- 编写一个 SQL 查询来实现分数排名。
--
-- 如果两个分数相同，则两个分数排名（Rank）相同。请注意，平分后的下一个名次应该是下一个连续的整数值。换句话说，名次之间不应该有“间隔”。
--
-- +----+-------+
-- | Id | Score |
-- +----+-------+
-- | 1  | 3.50  |
-- | 2  | 3.65  |
-- | 3  | 4.00  |
-- | 4  | 3.85  |
-- | 5  | 4.00  |
-- | 6  | 3.65  |
-- +----+-------+
-- 例如，根据上述给定的 Scores 表，你的查询应该返回（按分数从高到低排列）：
--
-- +-------+------+
-- | Score | Rank |
-- +-------+------+
-- | 4.00  | 1    |
-- | 4.00  | 1    |
-- | 3.85  | 2    |
-- | 3.65  | 3    |
-- | 3.65  | 3    |
-- | 3.50  | 4    |
-- +-------+------+
-- 重要提示：对于 MySQL 解决方案，如果要转义用作列名的保留字，可以在关键字之前和之后使用撇号。例如 `Rank`

-- row_number()：依次递增排名，无重复排名
-- rank()：相同分数有重复排名，但是重复后下一个人按照实际排名
-- dense_rank()：分数一致排名一致，分数不一致排名+1
-- NTILE(4)：分组排名，里面的数字是几，最多排名就是几，里面的数字是4，最多的排名就是4

select Score, dense_rank() over (order by Score desc) as `Rank` from Scores
-- 不指定 partition by 相当于所有行数据一个 partition, 数据进行区内排序
-- dense_rank() 相当于每一行数据一个窗口, 对数据进行比较
