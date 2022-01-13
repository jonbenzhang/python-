"""
43. 字符串相乘
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = 0
        for i in range(l1):
            for j in range(l2):
                ans += (int(num1[i]) * int(num2[j])) * (10 ** (i + j))
        return str(ans)


if __name__ == '__main__':
    a = "10"
    b = "10"
    "56088"
    s = Solution()
    print(s.multiply(a, b))
