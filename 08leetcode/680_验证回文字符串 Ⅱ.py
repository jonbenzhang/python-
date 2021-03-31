"""
680. 验证回文字符串 Ⅱ
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(left, right):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return valid(l + 1, r) or valid(l, r - 1)
        return True


if __name__ == '__main__':
    a = "abca"
    s = Solution()
    print(s.validPalindrome(a))
