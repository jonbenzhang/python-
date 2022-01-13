"""
322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的。
"""
"""
方式1 动态规划
"""
from typing import List


# 方式1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        m = amount + 1
        nums = [-1] * m
        nums[0] = 0
        for coin in coins:
            for i in range(coin, m):
                if nums[i - coin] != -1:
                    nums[i] = nums[i - coin] + 1 if nums[i] == -1 else min(nums[i - coin] + 1, nums[i])
        return nums[-1]
