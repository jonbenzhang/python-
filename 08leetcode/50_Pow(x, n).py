"""
50. Pow(x, n)
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，x^n）。
示例 1：
输入：x = 2.00000, n = 10
输出：1024.00000
"""





class Solution:
    def myPow(self, x: float, n: int) -> float:
        def p(n):
            if n == 0:
                return 1
            y = p(n // 2)
            # n&1判断奇偶数
            return y * y * x if n & 1 else y * y
            # 不要使用p(n // 2)*p(n // 2)
        if n < 0:
            return 1 / p(-n)
        else:
            return p(n)


if __name__ == '__main__':
    print(Solution.myPow(2.00, 10))
