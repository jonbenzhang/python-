"""
917. 仅仅反转字母
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。
"""

import string


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        s = list(S)
        left, right = 0, len(S) - 1

        while left < right:
            if ord(s[left]) < ord("A") or ord(s[left]) > ord("z") or ord('Z') < ord(s[left]) < ord('a'):
                left += 1
                continue
            if ord(s[right]) < ord("A") or ord(s[right]) > ord("z") or ord('Z') < ord(s[right]) < ord('a'):
                right -= 1
                continue
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)
