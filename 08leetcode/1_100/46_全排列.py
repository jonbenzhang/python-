"""
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
"""
"""
方式1 回溯算法
"""
from typing import List


# 方式1
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(nums, tmp):
            if not nums:
                results.append(tmp)
            for i in range(len(nums)):
                backtrack(nums[0:i] + nums[i + 1:], [nums[i]] + tmp)

        backtrack(nums, [])
        return results
