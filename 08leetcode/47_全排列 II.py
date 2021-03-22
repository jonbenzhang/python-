"""
47. 全排列 II
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
"""
"""
回溯法
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        def backtrack(nums, tmp):
            if not nums:
                results.append(tmp)
            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i - 1]:
                    continue
                backtrack(nums[0:i] + nums[i + 1:], [nums[i]] + tmp)

        backtrack(nums, [])
        return results
