"""
122. 买卖股票的最佳时机 II
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。
注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
"""
"""
方式1 贪心算法 Greedy
方式2 动态规划
"""
from typing import List

# 方式1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        yesterday_price = prices[0]
        profit = 0
        for i in prices[1:]:
            if i > yesterday_price:
                profit += (i - yesterday_price)
            yesterday_price = i
        return profit
# 方式2
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        dp = [[0, 0] for _ in range(size)]
        dp[0][1] = -prices[0]
        for i in range(1,size):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]