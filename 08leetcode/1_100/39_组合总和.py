"""
39. 组合总和
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的数字可以无限制重复被选取。
说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
"""
"""
方式1 回溯算法
"""
from typing import List

"""
方式1,重要的是要进行排序，不能往回找,否则会出现重复
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        # 要进行排序
        candidates.sort()
        results = []

        def backtrack(index, tmp):
            tmp_sum = sum(tmp)
            if tmp_sum > target:
                return
            elif tmp_sum == target:
                results.append(tmp)
                return
            else:
                for i in range(index, size):
                    # 从当前的第i个元素，可以继续使用
                    backtrack(i, [candidates[i]] + tmp)

        backtrack(0, [])
        return results


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []

        def backtrack(nums, target, tmp):
            if target == 0:
                results.append(tmp)
            elif target < 0 or not nums:
                return
            else:
                for i in range(len(nums)):
                    backtrack(nums[i:], target - nums[i], [nums[i]] + tmp)

        backtrack(candidates, target, [])
        return results
