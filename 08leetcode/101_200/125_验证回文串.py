"""
125. 验证回文串
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
说明：本题中，我们将空字符串定义为有效的回文串。
"""
"""
方式1 去掉非字母，把大写转为小写
方式2 双指针直接判断
"""

import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = "".join([i.lower() for i in s if s.isalnum()])
        return s2 == s2[::-1]


class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True
