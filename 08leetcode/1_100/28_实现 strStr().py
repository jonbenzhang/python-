"""
28. 实现 strStr()
实现 strStr() 函数。
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
"""
"""
方式1 暴力匹配
方式2 Rabin Karp(进行哈希计算后匹配哈希值)
"""


# 方式1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)
        for start in range(n - L + 1):
            if haystack[start: start + L] == needle:
                return start
        return -1


# 方式2
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)
        if h_len<n_len:
            return -1
        if not needle:
            return 0
        h_hash = lambda i: ord(haystack[i]) - ord('a')
        n_hash = lambda i: ord(needle[i]) - ord('a')
        hash_n = 26
        needle_hash, haystack_hash = 0, 0
        for i in range(n_len):
            needle_hash = hash_n * needle_hash + n_hash(i)
            haystack_hash = hash_n * haystack_hash + h_hash(i)
        if needle_hash == haystack_hash:
            return 0
        for i in range(1, h_len - n_len + 1):
            haystack_hash = (haystack_hash - h_hash(i-1) * hash_n ** (n_len - 1)) * hash_n + h_hash(i + n_len-1)
            if haystack_hash == needle_hash:
                return i

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.strStr("gcab", "ab"))
