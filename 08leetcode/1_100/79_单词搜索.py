"""
79. 单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
"""
"""
方式１　dfs
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, k):

            if board[i][j] == word[k]:
                if k == len(word)-1:
                    return True
                tmp = board[i][j]
                board[i][j] = ""
                for i1, j1 in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    if 0 <= i + i1 < m and 0 <= j + j1 < n:
                        if dfs(i + i1, j + j1, k + 1):
                            return True
                board[i][j] = tmp

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
