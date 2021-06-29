"""
44. 通配符匹配
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        # if not m and p == "*" * n:
        #     return True
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    if dp[i - 1][j - 1]:
                        dp[i][j] = True
                    # if j > 1 and p[j - 2] == "*" and dp[i - 1][j - 2]:
                    #     dp[i][j] = True
                elif p[j - 1] == "*":
                    # dp[i - 1][j - 1] or
                    if dp[i - 1][j] or dp[i][j - 1]:
                        dp[i][j] = True

        # [print(i) for i in dp]
        return dp[-1][-1]


if __name__ == '__main__':
    a = "ho"
    b = "**ho"
    s = Solution()
    print(s.isMatch(a, b))
