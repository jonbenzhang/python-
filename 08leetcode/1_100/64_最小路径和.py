"""
64. 最小路径和
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
"""
"""
方式1 动态规划
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        dp = grid
        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                dp[i][j] = min(dp[i - 1][j] if i - 1 >= 0 else float("inf"), dp[i][j - 1] if j - 1 >= 0 else float("inf")) + grid[i][j]
        return dp[-1][-1]


if __name__ == '__main__':
    s = Solution()
    print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
