"""
78. 子集
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        def backtrack(nums, tmp):
            results.append(tmp)
            for i in range(len(nums)):
                backtrack(nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return results
