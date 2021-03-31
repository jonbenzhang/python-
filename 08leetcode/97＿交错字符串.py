"""
97. 交错字符串
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
提示：a + b 意味着字符串 a 和 b 连接。
"""
"""
方式1 动态规划
"""


# 方式1
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if s1 == "":
            if s2 == s3:
                return True
            else:
                return False
        if s2 == "":
            if s1 == s3:
                return True
            else:
                return False
        m = len(s1)
        n = len(s2)
        if m + n != len(s3):
            return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # 先初始化两个边界
        if s1[0] == s3[0]:
            dp[1][0] = True
        if s2[0] == s3[0]:
            dp[0][1] = True
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if i >= 1 and s3[i + j - 1] == s1[i - 1] and dp[i - 1][j]:
                    dp[i][j] = True
                if j >= 1 and s3[i + j - 1] == s2[j - 1] and dp[i][j - 1]:
                    dp[i][j] = True
        return dp[-1][-1]


if __name__ == '__main__':
    a = "aabcc"
    b = "dbbca"
    c = "aadbbcbcac"
    s = Solution()
    print(s.isInterleave(a, b, c))
