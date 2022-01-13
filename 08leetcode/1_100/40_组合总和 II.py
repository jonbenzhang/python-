"""
40. 组合总和 II
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。
"""
"""
方式1 回溯
"""
# 方式1
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        # 要排序
        candidates.sort()
        size = len(candidates)

        def backtrack(index, target, tmp):
            if target == 0:
                results.append(tmp)
            elif target < 0:
                return
            else:
                for i in range(index, size):
                    # 重要步骤防止出现，重复列表
                    # 如[1,1,2]，会出现两个[1,2]
                    if i > index and candidates[i] == candidates[i - 1]:
                        continue
                    backtrack(i + 1, target - candidates[i], tmp + [candidates[i]])

        backtrack(0, target, [])
        return results
