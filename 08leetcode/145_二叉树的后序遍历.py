"""
145. 二叉树的后序遍历
给你二叉树的根节点 root ，返回它节点值的 后序 遍历。
"""
"""
方式1 递归
方式2 迭代
"""
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                l.append(root.val)

        l = []
        postorder(root)
        return l


# 方式2
# 后序是左右中,也就是中右左的反转
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        results = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return results[::-1]

