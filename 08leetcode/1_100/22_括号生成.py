"""
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""
"""
方式1 递归
"""
from typing import List


# 方式1
class Solution:
    def recursion(self, left, right, s, results, n):
        if left == n and right == n:
            results.append(s)
            return
        if left < n:
            self.recursion(left + 1, right, s + "(", results, n)
        if left > right:
            self.recursion(left, right + 1, s + ")", results, n)
        return

    def generateParenthesis(self, n: int) -> List[str]:
        results = []
        self.recursion(0, 0, "", results, n)
        return results
