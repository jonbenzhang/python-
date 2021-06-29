"""
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
"""
"""
方式1 动态规划
"""
from typing import List


class Solution:
    @classmethod
    def maxProduct(self, nums: List[int]) -> int:
        min_v = nums[0]
        max_v = nums[0]
        ans = nums[0]
        for i in range(1, len(nums)):
            min_v,max_v = min(nums[i], nums[i] * min_v, nums[i] * max_v),max(nums[i], nums[i] * min_v, nums[i] * max_v)
            ans = max(max_v, ans)
        return ans  


if __name__ == '__main__':
    Solution.maxProduct([2, 3, -2, 4])
