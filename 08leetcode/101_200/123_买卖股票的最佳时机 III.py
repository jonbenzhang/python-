"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
"""5444444444444444444444444444444444444444444444
方式1 动态规划
"""

from typing import List

# 方式1
"""
123 状态转移方程
T[i][2][0] = max(T[i - 1][2][0], T[i - 1][2][1] + prices[i])
T[i][2][1] = max(T[i - 1][2][1], T[i - 1][1][0] - prices[i])
T[i][1][0] = max(T[i - 1][1][0], T[i - 1][1][1] + prices[i])
T[i][1][1] = max(T[i - 1][1][1], T[i - 1][0][0] - prices[i]) = max(T[i - 1][1][1], -prices[i])
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        nums = [[[0, 0], [0, 0], [0, 0]] for _ in range(size)]
        nums[0][0][0] = 0
        nums[0][1][1] = -prices[0]
        nums[0][2][0] = 0
        nums[0][2][1] = -prices[0]
        for i in range(1, size):
            nums[i][1][1] = max(nums[i - 1][1][1], nums[i - 1][0][0] - prices[i])
            nums[i][1][0] = max(nums[i - 1][1][0], nums[i - 1][1][1] + prices[i])
            nums[i][2][1] = max(nums[i - 1][2][1], nums[i - 1][1][0] - prices[i])
            nums[i][2][0] = max(nums[i - 1][2][0], nums[i - 1][2][1] + prices[i])
        return nums[-1][2][0]
