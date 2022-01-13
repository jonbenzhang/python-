"""
100. 相同的树
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(tree1, tree2):
            if not tree1 or not tree2:
                return tree1 == tree2
            if tree1.val != tree2.val:
                return False

            return dfs(tree1.left, tree2.left) and dfs(tree1.right, tree2.right)

        return dfs(p, q)
