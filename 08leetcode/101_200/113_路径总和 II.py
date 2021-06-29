"""
113. 路径总和 II
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。
叶子节点 是指没有子节点的节点。
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        results = []

        def dfs(target, root, path):
            if not root.left and not root.right:
                nonlocal results
                if target == targetSum:
                    results.append(path)
            if root.left:
                dfs(target + root.left.val, root.left, path+[root.left.val])
            if root.right:
                dfs(target + root.right.val, root.right, path+[root.right.val])

        dfs(root.val, root, [root.val])
        return results
