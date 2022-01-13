"""
190. 颠倒二进制位
颠倒给定的 32 位无符号整数的二进制位。
"""
"""
方式1 位运算
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        b = 0
        for _ in range(32):
            # 或使用下一行代码,不可以去掉括号（加减的优先级高于位移(>>、<<)）
            # b = (b << 1) + (n & 1)
            b = b << 1 | n & 1
            n = n >> 1
        return b
