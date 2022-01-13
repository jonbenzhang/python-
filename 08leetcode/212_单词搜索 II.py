"""
212. 单词搜索 II
给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
"""
"""
方式1 tried 树
"""

from typing import List


# 方式1
class Solution:
    @classmethod
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        results = set()
        m = len(board)
        n = len(board[0])
        tree = {}
        for word in words:
            node = tree
            for i in word:
                if i not in node:
                    node[i] = {}
                node = node[i]
            node["#"] = "#"

        def dfs(i, j, cur_tree, current_word):
            tmp = board[i][j]
            board[i][j] = ""
            if "#" in cur_tree:
                results.add(current_word)
            for i1, j1 in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if 0 <= i + i1 < m and 0 <= j + j1 < n and board[i + i1][j + j1] in cur_tree:
                    dfs(i + i1, j + j1, cur_tree[board[i + i1][j + j1]], current_word + board[i + i1][j + j1])
            board[i][j] = tmp

        for i in range(m):
            for j in range(n):
                if board[i][j] in tree:
                    dfs(i, j, tree[board[i][j]], board[i][j])
        return list(results)
if __name__ == '__main__':
    a = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
    b = ["oath", "pea", "eat", "rain"]
    Solution.findWords(a,b)