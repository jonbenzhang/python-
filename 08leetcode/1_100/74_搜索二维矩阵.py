"""
74. 搜索二维矩阵
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
"""
"""
方式1  二分法
"""
from typing import List


# 方式1   
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m * n - 1
        while left <= right:
            mid = (left + right) // 2
            i = mid // n
            j = mid % n
            if target == matrix[i][j]:
                return True
            elif target < matrix[i][j]:
                right = mid - 1
            else:
                left = mid + 1
        return False
