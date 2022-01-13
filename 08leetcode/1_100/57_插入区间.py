"""
57. 插入区间
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
"""
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        results = []
        intervals.append(newInterval)
        intervals.sort(key=lambda a: a[0])
        for left, right in intervals:
            if not results:
                results.append([left, right])
                continue
            if left <= results[-1][1]:
                results[-1][1] = max(right, results[-1][1])
            else:
                results.append([left, right])
        return results
