"""
433. 最小基因变化
一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。
假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。
例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。
与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。
现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。
注意：
起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
如果一个起始基因序列需要多次变化，那么它每一次变化之后的基因序列都必须是合法的。
假定起始基因序列与目标基因序列是不一样的。
"""
"""
方式1 bfs
"""

from typing import List
from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank_set = set(bank)
        visited = set()
        if end not in bank_set:
            return -1
        q = deque([start])
        level = 0
        while q:
            level += 1
            if level > len(bank_set): return 0
            for _ in range(len(q)):
                word = q.popleft()
                word_list = list(word)
                for i in range(len(word_list)):
                    for j in ["A", "C", "G", "T"]:
                        tmp = word_list[i]
                        word_list[i] = j
                        s = "".join(word_list)
                        if s == end:
                            return level
                        if s in bank and s not in visited:
                            q.append(s)
                            visited.add(s)
                        word_list[i] = tmp
        return -1
