"""
hit hot dot  dog cog
127. 单词接龙
字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列：
序列中第一个单词是 beginWord 。
序列中最后一个单词是 endWord 。
每次转换只能改变一个字母。
转换过程中的中间单词必须是字典 wordList 中的单词。
给你两个单词 beginWord 和 endWord 和一个字典 wordList ，找到从 beginWord 到 endWord 的 最短转换序列 中的 单词数目 。如果不存在这样的转换序列，返回 0。
"""
"""
方式1 bfs
方式2 双向bfs
"""
from typing import List
from collections import deque


# 方式1_1
# 会超时
# 单词比较的时间复杂度为 n*wordLen
class Solution:
    @classmethod
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        visited = set()

        def compare(s1, s2):
            sum_s = 0
            for j in range(len(word)):
                if s1[j] != s2[j]:
                    sum_s += 1
            if sum_s == 1:
                return True
            else:
                return False

        level = 1
        q = deque()
        q.append(beginWord)

        while q:
            level += 1

            if level >= len(wordList) + 1:
                return 0
            for _ in range(len(q)):
                word = q.popleft()
                if word not in visited:
                    visited.add(word)
                else:
                    continue
                if compare(word, endWord):
                    return level
                for i in wordList:
                    if compare(word, i):
                        q.append(i)
        return 0


# 方式1_2
# bfs
# 单词比较的时间复杂度为 26*wordLen
class Solution:
    @classmethod
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        visited = set()
        level = 0
        q = deque()
        q.append(beginWord)

        while q:
            level += 1

            if level >= len(wordList) + 1:
                return 0
            for _ in range(len(q)):
                word = q.popleft()
                if word not in visited:
                    visited.add(word)
                else:
                    continue
                word_l = list(word)
                for i in range(len(word_l)):
                    tmp = word_l[i]
                    for j in range(26):
                        word_l[i] = chr(ord('a') + j)
                        s = "".join(word_l)
                        if s == endWord:
                            return level + 1
                        if s in wordList:
                            q.append(s)
                    word_l[i] = tmp
        return 0


import string


# 方式2
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        front = {beginWord}
        back = {endWord}
        dist = 1
        wordList = set(wordList)
        word_len = len(beginWord)
        while front:
            dist += 1
            next_front = set()
            for word in front:
                for i in range(word_len):
                    for c in string.ascii_lowercase:
                        if c != word[i]:
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word in back:
                                return dist
                            if new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word)
            front = next_front
            if len(back) < len(front):
                front, back = back, front
        return 0


if __name__ == '__main__':
    print(Solution.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
