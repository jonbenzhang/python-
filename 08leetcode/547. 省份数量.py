"""
547. 省份数量
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
返回矩阵中 省份 的数量。
"""
"""
方式1 并查集
"""
from typing import List


# 方式1
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        # 创建初始并查集的存储使用列表
        p = list(range(n))
        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] == 1:
                    self.union(p, i, j)
        return len({self.parent(p, i) for i in p})

    def union(self, p, i, j):
        """
        融合i和j两个元素的并查集
        :param p: 存储并查集的列表
        :param i: 元素i
        :param j: 元素j
        :return:
        """
        parent_i = self.parent(p, i)
        parent_j = self.parent(p, j)
        p[parent_i] = parent_j

    def parent(self, p, i):
        """
        找到元素i在并查集中的头元素
        :param p: 存储并查集的列表
        :param i: 元素i
        :return:
        """
        root = i
        while p[root] != root:
            # 获取头元素
            root = p[root]
        while p[i] != i:
            # 把前面的元素直接指向头元素
            x = i
            i = p[i]
            p[x] = root
        return root
