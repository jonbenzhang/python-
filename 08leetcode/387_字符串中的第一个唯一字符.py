"""
387. 字符串中的第一个唯一字符
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
"""
from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = OrderedDict()
        for i in s:
            d.setdefault(i, 0)
            d[i] += 1
        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
        return -1
