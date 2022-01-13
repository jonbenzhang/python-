"""
746. 使用最小花费爬楼梯
数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。

每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。

请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。
"""
"""
方式1 动态规划
"""
from typing import List


# 方式1
# 状态转移方程
# dp[i]=max(dp[i-1],dp[i-2])+cost[i]　
# dp[0]=0
# dp[1]=0
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_len = len(cost)
        cost.append(0)
        dp = cost
        for i in range(2, cost_len + 1):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.minCostClimbingStairs([0, 1, 1, 0]))