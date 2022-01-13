"""
111. 二叉树的最小深度
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明：叶子节点是指没有子节点的节点。
"""
"""
方式1 广度优先
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 方式1
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        q = deque()
        if root:
            q.append(root)
        else:
            return 0
        level = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    if node.left is None and node.right is None:
                        return level
                    q.append(node.left)
                    q.append(node.right)
            level += 1
