"""
36. 有效的数独
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次
"""
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        lines = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in rows[i]:
                        return False
                    else:
                        rows[i].add(board[i][j])
                    if board[i][j] in lines[j]:
                        return False
                    else:
                        lines[j].add(board[i][j])
                    if board[i][j] in boxes[i//3*3+j//3]:
                        return False
                    else:
                        boxes[i//3*3+j//3].add(board[i][j])
        return True
