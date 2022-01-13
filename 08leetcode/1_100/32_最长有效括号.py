"""
32. 最长有效括号
给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。
"""
"""
方式1 使用栈
方式2 动态规划
"""
"""
方式1
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        count = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                if stack:
                    count.append(stack.pop())
                    count.append(i)
        ans, n = 0, 1
        count.sort()
        for i in range(len(count) - 1):
            if count[i + 1] == count[i] + 1:
                n += 1
            else:
                ans = max(ans, n)
                n = 1

        return max(ans, n if n != 1 else 0)


# 方式2
# 状态转移方程
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                if s[i - 1] == ")":
                    if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                    else:
                        dp[i] = 0
        return max(dp)


if __name__ == '__main__':
    b = "(()) )())("
    print(len(b))
    s = Solution()
    print(s.longestValidParentheses(b))
