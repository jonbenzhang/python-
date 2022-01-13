"""
30. 串联所有单词的子串
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。
注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。
"""
"""
方式1 
方式2
看的泡菜的思路
"""
from typing import List
from collections import Counter


# 方式1　以单词总长度判断字符串是否符合
# 因为单词长度固定的，我们可以计算出截取字符串的单词个数是否和 words 里相等，所以我们可以借用哈希表。
#
# 一个是哈希表是 words，一个哈希表是截取的字符串，比较两个哈希是否相等！
#
# 因为遍历和比较都是线性的，所以时间复杂度：O(n^2)

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        results = []
        word_len = len(words[0])
        words_len = len(words)
        s_len = len(s)
        c = Counter(words)
        for i in range(s_len - word_len * words_len + 1):
            c2 = Counter()
            for j in range(i, i + word_len * words_len, word_len):
                c2[s[j:j + word_len]] += 1
            if c2 == c:
                results.append(i)
        return results


# 方式2
# 滑动窗口！
# 我们一直在 s 维护着所有单词长度总和的一个长度队列！
# 时间复杂度：O(n)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        results = []
        word_len = len(words[0])
        words_len = len(words)
        s_len = len(s)
        c = Counter(words)
        for start in range(word_len):
            left = start
            l = 0
            c2 = Counter()
            for i in range(start, s_len, word_len):
                word_new = s[i:i + word_len]
                # 每个单词统计的数
                c2[word_new] += 1
                # 有的单词的个数
                l += 1
                while c2[word_new] > c[word_new]:
                    c2[s[left:left + word_len]] -= 1
                    left += word_len
                    l -= 1
                if l==words_len:
                    results.append(left)

        return results

if __name__ == '__main__':
    a = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    b = ["fooo","barr","wing","ding","wing"]
    s =Solution()
    print(s.findSubstring(a, b))