"""
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""
"""
方式１ 枚举判断每一个柱子上方的最大存水量
方式2 单调栈
"""
from typing import List


# 方式1
# 时间过长
class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        ans = 0
        for i in range(size):
            l_max, r_max = 0, 0
            for l in range(i):
                l_max = max(l_max, height[l])
            for r in range(i + 1, size):
                r_max = max(r_max, height[r])
            ans += max(min(l_max, r_max) - height[i], 0)
        return ans


# 方式2
class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        size= len(height)
        for i in range(size):
            while stack and height[i]>height[stack[-1]]:
                idx = stack.pop()
                while stack and height[stack[-1]]==height[idx]:
                    stack.pop()
                if stack:
                    ans += (min(height[i],height[stack[-1]])-height[idx])*(i-stack[-1]-1)
            stack.append(i)
        return ans