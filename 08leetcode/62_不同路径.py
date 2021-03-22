"""
62. 不同路径
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
"""
"""
方式1 动态规划
"""


# 方式1
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        nums = [[0] * (n + 1) for _ in range(m + 1)]
        nums[m - 1][n - 1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                nums[i][j] = nums[i + 1][j] + nums[i][j + 1]
        return nums[0][0]
