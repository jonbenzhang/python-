"""
200. 岛屿数量
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。
"""
"""
方式1 dfs沉岛法
方式2 并查集

"""
from typing import List
from collections import deque


# 方式1_1
# 使用下面的方式1_2
class Solution:
    @classmethod
    def numIslands(self, grid: List[List[str]]) -> int:
        x = len(grid[0])
        y = len(grid)
        count = 0

        def judge():
            q = deque()
            sign = False
            for i in range(y):
                for j in range(x):
                    if grid[i][j] == "1":
                        q.append([i, j])
                        grid[i][j] = "0"
                        nonlocal count
                        count += 1
                        sign = True
                        break
                if sign:
                    break
            if not sign:
                return
            while q:
                i, j = q.popleft()
                if i - 1 >= 0 and grid[i - 1][j] == "1":
                    grid[i - 1][j] = "0"
                    q.append([i - 1, j])
                if i + 1 < y and grid[i + 1][j] == "1":
                    grid[i + 1][j] = "0"
                    q.append([i + 1, j])
                if j - 1 >= 0 and grid[i][j - 1] == "1":
                    grid[i][j - 1] = "0"
                    q.append([i, j - 1])
                if j + 1 < x and grid[i][j + 1] == "1":
                    grid[i][j + 1] = "0"
                    q.append([i, j + 1])

            judge()

        judge()
        return count


# 方式1_2
# 下面这种方法,至进行了一次遍历，而且结果更加简洁
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x = len(grid[0])
        y = len(grid)
        count = 0

        def dfs(i, j):
            if 0 <= i < y and 0 <= j < x and grid[i][j] == "1":
                grid[i][j] = "0"
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)

        for i in range(y):
            for j in range(x):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count


# 方式2_1
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.count = 0
        m = len(grid)
        n = len(grid[0])
        p_len = m * n
        p = list(range(p_len))

        def dfs(p, i, j):
            grid[i][j] = "0"
            self.count += 1
            for x, y in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                if 0 <= i + y < m and 0 <= j + x < n and grid[i + y][j + x] == "1":
                    self.union(p, n * i + j, n * (i + y) + (j + x))
            grid[i][j] = "1"

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(p, i, j)
        # 不能使用像547一样使用len({self.parent(p, i) for i in p}),因为有的元素对应为海水,不应该有并查集
        return self.count

    def union(self, p, i, j):
        parent_i = self.parent(p, i)
        parent_j = self.parent(p, j)
        if parent_j != parent_i:
            p[parent_i] = parent_j
            self.count -= 1

    def parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != root:
            x = i
            p[x] = root
            i = p[x]
        return root


# 方式2_2,使用字典做并查集
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.p = {}
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            self.parent(n * i + j)
            grid[i][j] = "0"
            for x, y in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                if 0 <= i + y < m and 0 <= j + x < n and grid[i + y][j + x] == "1":
                    self.union(n * i + j, n * (i + y) + (j + x))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
        return len({self.parent(i) for i in self.p.values()})

    def union(self, i, j):
        parent_i = self.parent(i)
        parent_j = self.parent(j)
        if parent_j != parent_i:
            self.p[parent_i] = parent_j

    def parent(self, i):
        self.p.setdefault(i, i)
        root = i
        while self.p[root] != root:
            root = self.p[root]
        while self.p[i] != root:
            x = i
            self.p[x] = root
            i = self.p[x]
        return root


if __name__ == '__main__':
    b = [["1", "1", "1"],
         ["0", "1", "0"],
         ["1", "1", "1"]]
    b = [["1", "1", "1", "1", "0"],
         ["1", "1", "0", "1", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "0", "0", "0"]]
    b = [["1", "1", "0", "0", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "1", "0", "0"],
         ["0", "0", "0", "1", "1"]]
    s = Solution()
    print(s.numIslands(b))
