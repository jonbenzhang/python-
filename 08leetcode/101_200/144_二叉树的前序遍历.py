"""
144. 二叉树的前序遍历
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
"""
"""
方式1 递归
方式2 迭代
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方式1
class Solution:
    def preorder(self, root: TreeNode, d):
        if root:
            d.append(root.val)
            self.preorder(root.left, d)
            self.preorder(root.right, d)

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        d = []
        self.preorder(root, d)
        return d


# 方式2
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        results = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return results
