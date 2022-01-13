"""
438. 找到字符串中所有字母异位词
给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。

字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
说明：
字母异位词指字母相同，但排列不同的字符串。
不考虑答案输出的顺序。
"""
"""
方式1 双指针加哈希
"""
from typing import List


# 方式1_1
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_l = len(s)
        p_l = len(p)
        results = []
        if s_l < p_l:
            return results
        d = {i: 0 for i in p}
        d2 = d.copy()
        for i in p:
            d2[i] += 1
        i, j = 0, p_l - 1
        for q in s[:p_l]:
            if q in d:
                d[q] += 1
        if d == d2:
            results.append(0)
        while j < s_l - 1:
            if s[i] in d:
                d[s[i]] -= 1
            i += 1
            j += 1
            if s[j] in d:
                d[s[j]] += 1
            if d == d2:
                results.append(i)
        return results


# 方式1_2
# 把方式1_1的代码进行整理
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_l = len(s)
        p_l = len(p)
        results = []
        if s_l < p_l:
            return results
        d = {i: 0 for i in p}
        d2 = d.copy()
        for i in p:
            d2[i] += 1
        i, j = 0, 0
        while j < s_l:
            if s[j] in d:
                d[s[j]] += 1
            if j - i == p_l:
                if s[i] in d:
                    d[s[i]] -= 1
                i += 1
            j += 1
            if d == d2:
                results.append(i)
        return results


if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))
