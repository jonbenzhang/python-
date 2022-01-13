"""
60. 排列序列
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。
"""
import math
"""
方式1 从最高位开始选择数字
"""

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = 0
        l = list(range(1, n + 1))
        for i in range(n - 1, 0, -1):
            b = math.factorial(i)
            a, b = divmod(k - 1, b)
            result = result * 10 + l[a]
            k = b + 1
            # print(a)
            del l[a]
        result = result * 10 + l[0]
        return str(result)


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(3, 1))
