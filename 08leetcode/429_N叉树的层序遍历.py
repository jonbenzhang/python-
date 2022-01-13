"""
429. N 叉树的层序遍历
给定一个 N 叉树，返回其节点值的层序遍历。（即从左到右，逐层遍历）。
树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。
 """
"""
方式1 bfs 广度优先搜索
"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        results = []
        q = deque()
        if root:
            q.append(root)
        while q:
            r = []
            for i in range(len(q)):
                node = q.popleft()
                r.append(node.val)
                for i in node.children:
                    q.append(i)
            results.append(r)
        return results
