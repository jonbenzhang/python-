"""
72. 编辑距离
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
你可以对一个单词进行如下三种操作：
插入一个字符
删除一个字符
替换一个字符
"""

"""
方式1 动态规划
"""
"""
方式1
状态转移方程
if i=j f(i,j)=f(i-1,j-1)
if i!=j f(i,j)=min(f(i-1,j),f(i,j-1),f(i-1,j-1))+1 
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if not m or not n:
            return max(m, n)
        dp = [[0] * (n+1) for _ in range(m+1)]
        dp[0] = [i for i in range(n+1)]
        for i in range(m+1):
            dp[i][0] = i
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]


if __name__ == '__main__':
    a = "a"
    b = "b"
    s = Solution()
    print(s.minDistance(a, b))
