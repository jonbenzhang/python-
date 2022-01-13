"""
98. 验证二叉搜索树
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
"""
"""
方式1 递归
方式2 中序遍历，搜索二叉树，中序遍历结果必然是从小到大的
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方式1
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def vri(root, lower=float("-inf"), upper=float("inf")):
            if root is None:
                return True
            val = root.val
            if val >= upper or val <= lower:
                return False
            if not vri(root.left, lower, val):
                return False
            if not vri(root.right, val, upper):
                return False
            return True

        return vri(root)


# 方式2
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        val = float("-inf")
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val <= val:
                return False
            else:
                val = node.val
            node = node.right
        return True
