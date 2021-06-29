"""
94. 二叉树的中序遍历
给定一个二叉树的根节点 root ，返回它的 中序 遍历。
"""
"""
方式1　递归
方式2 迭代使用栈
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方式１
class Solution:
    def inorder(self, root, d):
        if root:
            self.inorder(root.left, d)
            d.append(root.val)
            self.inorder(root.right, d)

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        d = []
        self.inorder(root, d)
        return d


# 方式2
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        results = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            results.append(cur.val)
            cur = cur.right

        return results

