"""
169. 多数元素
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素
"""
"""
# 哈希表法
"""
from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        n = len(nums) // 2
        for num in nums:
            d[num] += 1
            if d[num] > n:
                return num
