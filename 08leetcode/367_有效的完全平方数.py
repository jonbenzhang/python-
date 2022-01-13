"""
367. 有效的完全平方数
给定一个 正整数 num ，编写一个函数，如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

进阶：不要 使用任何内置的库函数，如  sqrt 。
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left, right = 1, num // 2
        while left <= right:
            mid = (left + right) // 2
            m = mid * mid
            if m == num:
                return True
            elif m > num:
                right = mid - 1
            else:
                left = mid + 1

        return False
