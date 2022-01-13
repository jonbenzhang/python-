"""
589. N 叉树的前序遍历
给定一个 N 叉树，返回其节点值的 前序遍历 。
N 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
"""
"""
方式1递归
方式2 迭代
"""
# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# 方式1
class Solution:
    def preorder_n(self, root, d):
        if root:
            d.append(root.val)
            if root.children:
                for child in root.children:
                    self.preorder_n(child, d)

    def preorder(self, root: 'Node') -> List[int]:
        d = []
        self.preorder_n(root, d)
        return d


# 方式2
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        results = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.children:
                for i in node.children[::-1]:
                    stack.append(i)
        return results
