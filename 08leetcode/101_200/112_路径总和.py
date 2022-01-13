"""
112. 路径总和
给你二叉树的根节点 root 和一个表示目标和的整数 targetSum ，判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。
叶子节点 是指没有子节点的节点。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        def dfs(target, root):
            if not root.left and not root.right:
                if target == targetSum:
                    return True
                else:
                    return False
            if root.left:
                if dfs(target + root.left.val, root.left):
                    return True
            if root.right:
                if dfs(target + root.right.val, root.right):
                    return True

            return False

        return dfs(root.val, root)
