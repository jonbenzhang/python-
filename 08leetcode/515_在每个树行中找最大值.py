"""515. 在每个树行中找最大值
您需要在二叉树的每一行中找到最大的值。
"""
"""
方式1 bfs
"""
from collections import deque
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        results = []
        q = deque()
        if root:
            q.append(root)
        while q:
            m = float("-inf")
            for _ in range(len(q)):
                node = q.popleft()
                m = max(node.val, m)
                results.append(m)
                q.append(node.left)
                q.append(node.right)
        return results
