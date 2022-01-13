"""
91. 解码方法
一条包含字母 A-Z 的消息通过以下映射进行了 编码 ：

'A' -> 1
'B' -> 2
...
'Z' -> 26
要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"111" 可以将 "1" 中的每个 "1" 映射为 "A" ，
从而得到 "AAA" ，或者可以将 "11" 和 "1"（分别为 "K" 和 "A" ）映射为 "KA" 。注意，"06" 不能映射为 "F" ，因为 "6" 和 "06" 不同。

给你一个只含数字的 非空 字符串 num ，请计算并返回 解码 方法的 总数 。
题目数据保证答案肯定是一个 32 位 的整数。
"""
"""
方式1 动态规划
"""

# 方式1
"""
如果 s[i-2]不为1或2:
    if s[i-1] 为0,那么不能解码
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        s_len = len(s)
        dp = [0] * (s_len + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, s_len+1):
            if s[i - 2] not in ['1', '2']:
                # 30,00等无法解码
                if s[i-1] == '0':
                    return 0
                dp[i] = dp[i - 1]
            elif s[i - 2] == '2' and int(s[i - 1]) > 6:
                dp[i] = dp[i - 1]
            elif s[i-1] == '0':
                dp[i] = dp[i - 2]
            else:
                dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.numDecodings("99"))
