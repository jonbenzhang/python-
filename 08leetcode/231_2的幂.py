"""
231. 2的幂
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
"""
"""
方式1 位运算
"""


# 2的幂的二进制数只有一个位置为1，其余位置均为0
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
