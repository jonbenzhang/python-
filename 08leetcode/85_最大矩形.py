"""
85. 最大矩形
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
"""

"""
方式1 使用单调递增的栈来实现
"""
from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        stack = []
        max_val = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            heights = []
            for j in range(n):
                height = 0
                for q in range(i, m):
                    if matrix[q][j] == "1":
                        height += 1
                    else:
                        break
                heights.append(height)
            max_val = max(max_val, self.largestRectangleArea(heights))

        return max_val

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
    a = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    s = Solution()
    print(s.maximalRectangle(a))
