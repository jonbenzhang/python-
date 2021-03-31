"""
115. 不同的子序列
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
题目数据保证答案符合 32 位带符号整数范围。
"""
"""
方式1 动态规划
方式2 dfs
"""
"""
方式１　状态转移方程
当 S[j] == T[i] , dp[i][j] = dp[i-1][j-1] + dp[i][j-1];

当 S[j] != T[i] , dp[i][j] = dp[i][j-1]
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0] = [1 for _ in range(n + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[j - 1] != t[i - 1]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
        return dp[-1][-1]


"""
方式2 dfs
"""


class Solution1:
    def numDistinct(self, s: str, t: str) -> int:
        count = 0

        def dfs(index, s):
            nonlocal count
            if s == t:
                count += 1
                return
            if len(s) <= len(t):
                return
            for i in range(index, len(s)):
                dfs(i, s[:i] + s[i + 1:])

        dfs(0, s)
        return count


if __name__ == '__main__':
    s = Solution()
    a = "rabbbit"
    b = "rabbit"
    print(s.numDistinct(a, b))
