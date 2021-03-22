"""
69. x 的平方根
实现 int sqrt(int x) 函数。
计算并返回 x 的平方根，其中 x 是非负整数。
由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
"""
"""
方式1 二分查找
方式2 牛顿迭代法
"""


# 方式1_1
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            m1 = mid * mid
            m2 = (mid + 1) * (mid + 1)
            if m1 <= x < m2:
                return mid
            elif m1 > x:
                right = mid - 1
            else:
                left = mid + 1


# 方式1_2
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x

        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return int(right)


# 方式2
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return int(r)
