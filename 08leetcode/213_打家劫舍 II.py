"""
213. 打家劫舍 II
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。
同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。
"""
"""
方式1 动态规划,就是把198号问题拆分为两个问题,去头和去尾
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def rob1(nums):
            pre, cur = 0, 0
            for num in nums:
                cur, pre = max(cur, pre + num), cur
            return cur

        return max(rob1(nums[1:]), rob1(nums[:-1]))
