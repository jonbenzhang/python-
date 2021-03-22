"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。
"""
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        def backtrack(nums, tmp):
            results.append(tmp)
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                backtrack(nums[i + 1:], tmp + [nums[i]])
        backtrack(nums, [])
        return results
