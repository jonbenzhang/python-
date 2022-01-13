"""
130. 被围绕的区域
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
"""
"""
方式1 dfs
方式2 并查集
"""
from typing import List


# 方式1,
# 1.把与边界相连的O,先转为A
# 2.把剩余的O转换为X,
# 3.A再转换为O

class Solution:
    @classmethod
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(i, j):
            # pai.add((i, j))
            board[i][j] = "A"
            for x, y in ((1, 0), (-1, 0), (0, - 1), (0, 1)):
                if 0 < i + y < m - 1 and 0 < j + x < n - 1 and board[i + y][j + x] == "O":
                    dfs(i + y, j + x)

        # 使用集合进行存储会出现超时
        # pai = set()
        m = len(board)
        n = len(board[0])
        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == 'O':
                    dfs(i, j)
        for i in range(1, m - 1):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    dfs(i, j)
        for i in range(m):
            for j in range(n):
                # if (i, j) not in pai:
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

        print(board)


# 方式2
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        self.p = {}
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if i in (0, m - 1) or j in (0, n - 1):
                        self.union(i * n + j, m * n)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if 0 <= i + x < m and 0 <= j + y < n and board[i + x][j + y] == "O":
                                self.union(i * n + j, (i + x) * n + (j + y))
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == "O" and self.find(i * n + j) != self.find(m * n):
                    board[i][j] = "X"
        print(self.p)

    def union(self, i, j):
        self.p[self.find(i)] = self.find(j)

    def find(self, i):
        self.p.setdefault(i, i)
        if self.p[i] != i:
            self.p[i] = self.find(self.p[i])
        return self.p[i]


if __name__ == '__main__':
    b = [["X", "X", "X", "X"],
         ["X", "O", "O", "X"],
         ["X", "X", "O", "X"],
         ["X", "O", "X", "X"]]
    b = [["O", "O"], ["O", "O"]]
    b = [["X", "O", "X"], ["X", "O", "X"], ["X", "O", "X"]]
    s = Solution()
    print(s.solve(b))
