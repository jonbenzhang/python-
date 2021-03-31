"""
541. 反转字符串 II
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。

如果剩余字符少于 k 个，则将剩余字符全部反转。
如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。
"""
from typing import List

# 方式1
# 弄负责了，看方式2的逻辑
class Solution:
    def reverseString(self, left, right, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        l = len(s_list)
        for i in range(2 * k, l, 2 * k):
            self.reverseString(i - 2 * k, i - 1 - k, s_list)

        n = (l - 1) // (2 * k)
        last_left = n * 2 * k
        last_right = min(l - 1, n * 2 * k + k - 1)
        self.reverseString(last_left, last_right, s_list)
        return "".join(s_list)

# 方式2
class Solution(object):
    def reverseStr(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)