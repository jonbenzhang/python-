"""
56. 合并区间
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
"""
"""
方式1 先按照左边界排序
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda a:a[0])
        results = []
        for l, r in intervals:
            if results and l <= results[-1][1]:
                results[-1][1] = max(r, results[-1][1])
            else:
                results.append([l, r])
        return results


if __name__ == '__main__':
    s = Solution()
    b = [[1, 4], [0, 4]]
    print(s.merge(b))

