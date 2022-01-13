"""
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。
"""
"""
方式1 暴力查找，枚举每一点然后向两边扩散
方式2 动态规划
"""


# 方式1
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 存储回文子串最大长度
        max_len = 0
        # 回文子串的左右边界
        l = 0
        r = 0

        def verification(left, right):
            nonlocal l, r, max_len
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > max_len:
                        l = left
                        r = right
                        max_len = r - l + 1
                    left -= 1
                    right += 1
                else:
                    break

        for i in range(len(s)):
            verification(i, i)
            if i < len(s) - 1:
                verification(i, i + 1)
        return s[l:r + 1]


# 方式2
# f(i,j)=True j<=i
# f(i,j) = s[i]==s[j] and f(i+1,j-1)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        left, right = 0, 0
        dp = [[True] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i + 1 >= max_len:
                        max_len = j - i + 1
                        left, right = i, j
                else:
                    dp[i][j] = False
        return s[left:right + 1]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome("aacabdkbcba"))
