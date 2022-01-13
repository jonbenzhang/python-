"""
37. 解数独
编写一个程序，通过填充空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。
"""
"""
方式1 dfs
"""
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        lines = [{i for i in range(1, 10)} for _ in range(9)]
        rows = [{i for i in range(1, 10)} for _ in range(9)]
        blocks = [{i for i in range(1, 10)} for _ in range(9)]
        point_list = []

        def dfs(level):
            if level == len(point_list):
                return True
            i, j = point_list[level]
            nums = rows[i] & lines[j] & blocks[i // 3 * 3 + j // 3]
            if nums:
                for num in nums:
                    rows[i].remove(num)
                    lines[j].remove(num)
                    blocks[i // 3 * 3 + j // 3].remove(num)
                    board[i][j] = str(num)
                    if dfs(level + 1):
                        return True
                    rows[i].add(num)
                    lines[j].add(num)
                    blocks[i // 3 * 3 + j // 3].add(num)

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    point_list.append([i, j])
                else:
                    rows[i].remove(int(board[i][j]))
                    lines[j].remove(int(board[i][j]))
                    blocks[i // 3 * 3 + j // 3].remove(int(board[i][j]))
        dfs(0)


if __name__ == '__main__':
    a = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s = Solution()
    s.solveSudoku(a)
    [print(i) for i in a]
