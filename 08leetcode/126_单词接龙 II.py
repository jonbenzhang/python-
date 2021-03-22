"""
126. 单词接龙 II
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换后得到的单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
"""
"""
方式1 bfs
"""
from typing import List
import collections
from collections import deque


# TODO 还没解决，时间过长没有通过
class Solution:
    @classmethod
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        end_sign = False
        results = []
        visited = set()
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        q = deque()
        q.append([beginWord])
        level = 0
        while q or end_sign or level < len(word_set) + 1:
            level += 1
            for _ in range(len(q)):
                path = q.popleft()
                word = path[-1]
                for i in range(len(word)):
                    for j in range(26):
                        s = word[0:i] + chr(ord('a') + j) + word[i + 1:]
                        if s in word_set and s not in visited:
                            path2 = path.copy()
                            path2.append(s)
                            if s == endWord:
                                if not end_sign:
                                    end_sign = True
                                results.append(path2)
                            else:
                                visited.add(s)
                                q.append(path2)
        return results


# 复制来的
class Solution2:
    @classmethod
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        cost = collections.defaultdict(lambda: float("inf"))
        cost[beginWord] = 0
        neighbors = collections.defaultdict(list)
        ans = []

        for word in wordList:
            for i in range(len(word)):
                neighbors[word[:i] + "*" + word[i + 1:]].append(word)
        q = collections.deque([[beginWord]])

        while q:
            path = q.popleft()
            cur = path[-1]
            if cur == endWord:
                ans.append(path.copy())
            else:
                for i in range(len(cur)):
                    for neighbor in neighbors[cur[:i] + "*" + cur[i + 1:]]:
                        if cost[cur] + 1 <= cost[neighbor]:
                            q.append(path + [neighbor])
                            cost[neighbor] = cost[cur] + 1
        return ans


if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    print(Solution.findLadders(beginWord, endWord, wordList))
