"""
84. 柱状图中最大的矩形
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
"""
"""
方式1,从i开始向两边遍历,直到到边界或者遇到小于当前柱子的停止(O(n^2)),包里放
方式2,单调栈
"""


# 方式1
# 时间过长无法通过
class Solution:
    def largestRectangleArea(self, heights) -> int:
        len_heights = len(heights)
        max_val = 0
        for i in range(len_heights):
            left = right = i
            end_sign = 0
            while end_sign != 2:
                end_sign = 0
                if left > 0 and heights[left - 1] >= heights[i]:
                    left -= 1
                else:
                    end_sign += 1
                if right < len_heights - 1 and heights[right + 1] >= heights[i]:
                    right += 1
                else:
                    end_sign += 1
                max_val = max(max_val, (right - left + 1) * heights[i])
        return max_val


from typing import List




class Solution:
    @classmethod
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_val = 0
        l = len(heights)
        for i in range(l):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()
                while stack and heights[stack[-1]] == heights[idx]:
                    stack.pop()
                max_val = max(heights[idx] * (i - 1 - (-1 if not stack else stack[-1])), max_val)
            stack.append(i)
        if stack:
            r_index = stack[-1]
            while stack:
                idx = stack.pop()
                max_val = max(heights[idx] * (r_index - (-1 if not stack else stack[-1])), max_val)
        return max_val


if __name__ == '__main__':
    print(Solution.largestRectangleArea([2, 1, 2]))
