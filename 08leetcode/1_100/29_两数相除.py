"""
29. 两数相除
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。
整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2
"""

"""
方式1 位运算
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        postive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        i, tmp = 1, divisor
        ans = 0
        while dividend > divisor << 1:
            divisor <<= 1
            i <<= 1
        while i:
            if dividend >= divisor:
                dividend -= divisor
                ans += i
            else:
                divisor >>= 1
                i >>= 1
        if not postive:
            ans = -ans
        return min(max(-2147483648, ans), 2147483647)


