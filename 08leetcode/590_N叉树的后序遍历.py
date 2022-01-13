"""
590. N 叉树的后序遍历
给定一个 N 叉树，返回其节点值的 后序遍历 。
N 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。
"""
"""
方法1,递归
方法2 迭代
"""
from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder_n(self, root, d):
        if root:
            if root.children:
                for i in root.children:
                    self.postorder_n(i, d)
            d.append(root.val)

    def postorder(self, root) -> List[int]:
        d = []
        self.postorder_n(root, d)
        return d

# 参考叉树的后序遍历
class Solution:
    def postorder(self, root) -> List[int]:
        results = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            node = stack.pop()
            results.append(node.val)
            for i in node.children:
                stack.append(i)
        return results[::-1]