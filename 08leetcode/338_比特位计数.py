"""
338. 比特位计数
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
"""
"""
方式1 位运算
"""
from typing import List


# 方式1
class Solution:
    def countBits(self, num: int) -> List[int]:
        results = [0] * (num + 1)
        for i in range(1, num + 1):
            if i & 1 == 1:
                # 奇数的1的个数等于,i-1的偶数中1的个数加1
                results[i] = results[i - 1] + 1
            else:
                # 偶数与它除以2所得的数1的个数相同
                results[i] = results[i >> 1]
        return results
