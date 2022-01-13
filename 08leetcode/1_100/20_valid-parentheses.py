"""
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
"""
"""
方式1 使用栈
"""

# 方式1
class Solution:
    # @classmethod
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for i in s:
            if i in d:
                stack.append(d[i])
            else:
                if len(stack) == 0 or i != stack.pop():
                    return False
        if len(stack):
            return False
        return True


if __name__ == '__main__':
    print(Solution.isValid("()[]{}"))
