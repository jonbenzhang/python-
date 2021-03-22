"""
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
 设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。
 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        size = len(prices)
        # maxProfit2可以不用创建
        # 这样优化了内存使用
        if k >= size >> 1:
            return self.maxProfit2(prices)
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(size)]
        for i in range(k + 1):
            dp[0][i][0] = 0
            dp[0][i][1] = -prices[0]
        for i in range(1, size):
            for j in range(1, k + 1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[-1][k][0]

    def maxProfit2(self, prices):
        print(prices)
        size = len(prices)
        dp = [[0, 0] for _ in range(size)]
        dp[0][1] = -prices[0]
        for i in range(1, size):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], - prices[i])
        return dp[-1][0]
