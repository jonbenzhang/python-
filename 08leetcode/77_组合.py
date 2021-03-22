"""
77. 组合
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
"""
"""

"""

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # nums = list(range(1, n + 1))
        results = []

        def recursion(index, result):
            # 减枝
            if index + k - len(result) > n:
                return
            if len(result) == k:
                results.append(result)
                return
            for i in range(index, n):
                tmp = result[:]
                # 列表i中对应的为i+1,所以去掉列表
                # tmp.append(nums[i])
                tmp.append(i+1)
                recursion(i + 1, tmp)

        recursion(0, [])

        return results
