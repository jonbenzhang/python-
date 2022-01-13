class Solution:
    @classmethod
    def isMatch(self, s: str, p: str) -> bool:
        s_l, p_l = len(s)+1, len(p)+1
        dp = [[False] * p_l for _ in range(s_l)]
        dp[0][0] = True
        for i in range(2, p_l, 2):
            if dp[0][i - 2] == True and p[i - 1] == "*":
                dp[0][i] = True
        for i in range(1,s_l):
            for j in range(1,p_l):
                if p[j - 1] == "*":
                    # 即将字符组合 p[j - 2] * 看作出现 0 次时，能否匹配
                    if dp[i][j - 2]:
                        dp[i][j] = True
                    # 即让字符 p[j - 2] 多出现 1 次时，能否匹配；
                    # elif dp[i-1][j-1] and s[i - 1] == p[j - 2]:
                    elif dp[i-1][j] and s[i - 1] == p[j - 2]:
                        dp[i][j] = True
                    elif dp[i-1][j] and p[j - 2] == ".":
                        dp[i][j] = True
                else:
                    if dp[i - 1][j - 1] and s[i - 1] == p[j - 1]:
                        dp[i][j] = True
                    elif dp[i - 1][j - 1] and p[j - 1] == ".":
                        dp[i][j] = True
        # print(dp)
        return dp[-1][-1]


class Solution1:
    @classmethod
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        # 初始化首行
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        # 状态转移
        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == '*':
                    if dp[i][j - 2]:
                        dp[i][j] = True  # 1.
                    elif dp[i - 1][j] and s[i - 1] == p[j - 2]:
                        dp[i][j] = True  # 2.
                    elif dp[i - 1][j] and p[j - 2] == '.':
                        dp[i][j] = True  # 3.
                else:
                    if dp[i - 1][j - 1] and s[i - 1] == p[j - 1]:
                        dp[i][j] = True  # 1.
                    elif dp[i - 1][j - 1] and p[j - 1] == '.':
                        dp[i][j] = True  # 2.
        print(dp)
        return dp[-1][-1]


print(Solution.isMatch("aaa", "a*"))
print(Solution1.isMatch("aaa", "ab*a*c*a"))
# "aaa"
# "ab*a*c*a"
