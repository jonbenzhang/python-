"""
198. 打家劫舍
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。
"""
"""
方式1 动态规划
"""
from typing import List


# 方式1_1 二维数组
# 使用二维数组存储抢了当前房子的最大值和没有抢当前房子的最大值
class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [[nums[0], 0]]
        for i in range(1, size):
            dp.append([dp[i - 1][1] + nums[i], max(dp[i - 1][0], dp[i - 1][1])])
        return max(dp[-1])


# 方式1_2
class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)

        if size == 0:
            return 0
        elif size == 1:
            return nums[0]
        else:
            dp = [0] * (size + 1)
            dp[1] = nums[0]
            dp[2] = nums[1]
            for i in range(3, size + 1):
                dp[i] = max(dp[i - 2], dp[i - 3]) + nums[i - 1]
        return max(dp)


# 方式1_3
class Solution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)

        if size == 0:
            return 0
        elif size == 1:
            return nums[0]
        else:
            if nums[0] > nums[1]:
                nums[1] = nums[0]
            for i in range(2, size):
                nums[i] = max(nums[i - 1], nums[i - 2] + nums[i])
        return nums[-1]


# 方式1_4
class Solution:
    def rob(self, nums: List[int]) -> int:
        pre, cur = 0, 0
        for num in nums:
            cur, pre = max(cur, pre + num), cur
        return cur
