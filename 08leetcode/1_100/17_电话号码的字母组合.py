"""
17. 电话号码的字母组合
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""
from typing import List

from collections import deque

"""
方式1 字符串转为数组
方式2 字符串直接操作
"""
# 使用数组(发现转为数组作用不大)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        results = []
        q = deque(digits)
        if digits == "":
            return []

        def recursion(q: deque, l: List):
            if not q:
                results.append("".join(l))
                return
            num = q.popleft()
            s = phone[num]
            for i in s:
                l.append(i)
                recursion(q, l)
                # 除去递归造成的数据修改

                l.pop()
            # 除去递归造成的数据修改
            q.appendleft(num)

        recursion(q, [])
        return results


# 使用字符串
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        results = []
        if digits == "":
            return []

        def recursion(str1, result):
            if not str1:
                results.append(result)
                return
            num = str1[0]
            s = phone[num]
            for i in s:
                recursion(str1[1:], result+i)

        recursion(digits, "")
        return results
