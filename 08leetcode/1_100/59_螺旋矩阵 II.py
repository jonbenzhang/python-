"""
59. 螺旋矩阵 II
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
"""
from typing import List


class Solution:
    def nums_set(self, matrix, i, j, i2, j2):
        # 读取外圈的数据,顺时针方向
        for q in range(j, j2 + 1):
            matrix[i][q] = self.get_count()
        for q in range(i + 1, i2 + 1):
            matrix[q][j2] = self.get_count()
        if i != i2:
            for q in range(j2 - 1, j - 1, -1):
                matrix[i2][q] = self.get_count()
        if j != j2:
            for q in range(i2 - 1, i, -1):
                matrix[q][j] = self.get_count()
        if i + 2 <= i2 and j + 2 <= j2:
            self.nums_set(matrix, i + 1, j + 1, i2 - 1, j2 - 1)

    def generateMatrix(self, n: int) -> List[List[int]]:
        self.count = 0
        matrix = [[0] * n for i in range(n)]
        self.nums_set(matrix, 0, 0, n - 1, n - 1)
        return matrix

    def get_count(self):
        self.count += 1
        return self.count
