"""
51. N 皇后
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
"""
from typing import List

"""
方式1
"""
# 方式1_1 dfs
class Solution:
    # @classmethod
    def solveNQueens(self, n: int) -> List[List[str]]:
        qi = [["."] * n for i in range(n)]
        results = []
        rows = set()
        bias = set()
        bias2 = set()

        def queen(line):
            if line == n:
                results.append(["".join(i) for i in qi])
                return
            for i in range(n):
                if i not in rows and i + line not in bias and i - line not in bias2:
                    rows.add(i)
                    bias.add(i + line)
                    bias2.add(i - line)
                    qi[i][line] = "Q"
                    queen(line + 1)
                    qi[i][line] = "."
                    rows.remove(i)
                    bias.remove(i + line)
                    bias2.remove(i - line)

        queen(0)
        return results


# 方式1_2
# 复制的别人的
def solveNQueens(self, n):
    def DFS(queens, xy_dif, xy_sum):
        p = len(queens)
        if p == n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p - q not in xy_dif and p + q not in xy_sum:
                DFS(queens + [q], xy_dif + [p - q], xy_sum + [p + q])

    result = []
    DFS([], [], [])
    return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in result]


if __name__ == '__main__':
    Solution.solveNQueens(4)
