"""
73. 矩阵置零
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
进阶：

一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个仅使用常量空间的解决方案吗？
"""
"""
方式1 先扫描一遍记录哪些行和列有0,然后进行置为0,额外空间O(m+n)
方式2  使用第一行和第一列进行记录第一行和第一列有没有0
"""
from typing import List

# 方式2
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        row_sign = 0 in matrix[0]
        line_sign = False
        for i in range(m):
            if matrix[i][0] == 0:
                line_sign = True
                break
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if row_sign:
            for i in range(n):
                matrix[0][i] = 0
        if line_sign:
            for i in range(m):
                matrix[i][0] = 0
