"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
"""
from typing import List

"""
方式1 纵向遍历
方式2 使用zip
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        low = ""
        strs.sort(key=lambda a: len(a))
        min_str = strs[0]
        end_sign = False
        for i in range(len(min_str)):
            for s in strs[1:]:
                if s[i] != min_str[i]:
                    end_sign = True
            if end_sign:
                break
            low += min_str[i]
        return low


# 方式2
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = ""
        for i in zip(*strs):
            b = set(i)
            if len(b) == 1:
                result += b.pop()
            else:
                break
        return result
