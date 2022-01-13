"""
52. N皇后 II
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
"""
"""
方式１　dfs+位运算
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(row, cols, pie, na):
            """
            :param row: 记录当前对应的行数
            :param cols: 记录不能使用的列的index,不能在同一列
            :param pie: 记录不能使用的列的index,不能在同一撇上
            :param na: 记录不能使用的列的index,不能在同一捺上
            :return:
            """
            if row == n:
                nonlocal count
                count += 1
                return
            bits = ~(cols | pie | na) & ((1 << n) - 1)
            while bits:
                l = bits & -bits
                bits = bits & bits - 1
                # 撇下一行，对应的不能使用的列向左移动一个位置
                # 捺下一行，对应的不能使用的列向右移动一个位置
                dfs(row + 1, cols | l, (pie | l) << 1, (na | l) >> 1)

        count = 0
        dfs(0, 0, 0, 0)
        return count
