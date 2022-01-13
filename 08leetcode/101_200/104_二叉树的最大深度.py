"""
104. 二叉树的最大深度
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
说明: 叶子节点是指没有子节点的节点。
"""
"""
方式1 递归
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方式1
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def persort(level, root, results):
            if not root:
                results.append(level)
                return
            persort(level + 1, root.left, results)
            persort(level + 1, root.right, results)

        results = []
        persort(0, root, results)
        return max(results)
