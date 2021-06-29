"""
54. 螺旋矩阵
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""
from typing import List


class Solution:
    def nums_set(self, matrix, i, j, i2, j2):
        # 读取外圈的数据,顺时针方向
        for q in range(j, j2 + 1):
            self.results.append(matrix[i][q])
        for q in range(i + 1, i2 + 1):
            self.results.append(matrix[q][j2])
        if i != i2:
            for q in range(j2 - 1, j - 1, -1):
                self.results.append(matrix[i2][q])
        if j != j2:
            for q in range(i2 - 1, i, -1):
                self.results.append(matrix[q][j])
        if i + 2 <= i2 and j + 2 <= j2:
            self.nums_set(matrix, i + 1, j + 1, i2 - 1, j2 - 1)

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.results = []
        self.nums_set(matrix, 0, 0, len(matrix) - 1, len(matrix[0]) - 1)
        return self.results


if __name__ == '__main__':
    a = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]
    s = Solution()
    print(s.spiralOrder(a))
