"""
48. 旋转图像
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
"""
"""
方式1 先按照水平线翻转,然后按照主对角线翻转
"""
from typing import List


# 方式1
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 水平对角线翻转
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m // 2):
            matrix[i], matrix[m - i - 1] = matrix[m - i - 1], matrix[i]
        # 主对角线翻转
        for i in range(m):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
