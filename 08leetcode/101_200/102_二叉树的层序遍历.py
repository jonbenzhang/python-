"""
102. 二叉树的层序遍历
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
示例：
二叉树：[3,9,20,null,null,15,7],
"""
"""
方式1 使用队列
"""
from typing import List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 方式1
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        q = deque()
        if root:
            q.append(root)
        while q:
            result_one = []
            for _ in range(len(q)):
                node = q.popleft()
                result_one.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            results.append(result_one)
        return results
