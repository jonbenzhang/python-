"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
注意：给定 n 是一个正整数。
"""
"""
第n阶台阶走法数=n-1阶+n-2阶
方式1,使用动态规划,保存到一维数组
方式2,修改动态规划，只保存需要的三个变量而不是保存整个数组(最优解)
方式3,递归
"""


# 方式1
class Solution:
    def climbStairs(self, n: int) -> int:
        l = [0] * (n + 1)
        l[0] = 1
        l[1] = 1
        for i in range(2, n + 1):
            l[i] = l[i - 1] + l[i - 2]
        return l[n]


# 方式2
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b, c = 1, 1, 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return c


# 方式3
class Solution:
    d = {}
    def recursion(self, n):
        if n == 1 or n == 0:
            return 1
        if n in self.d:
            return self.d[n]
        self.d[n] =  self.recursion(n - 1) + self.recursion(n - 2)
        return self.d[n]

    def climbStairs(self, n: int) -> int:
        return self.recursion(n)
