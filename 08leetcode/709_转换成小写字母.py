"""
709. 转换成小写字母
实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。
"""
"""
方式1 直接调用函数
方式2 遍历
"""

# 方式1
class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()

# 方式2
class Solution:
    def toLowerCase(self, str: str) -> str:
        s = []
        for i in str:
            if ord('A') <= ord(i) <= ord('Z'):
                s.append(chr(ord(i) + 32))
            else:
                s.append(i)
        return "".join(s)
