"""
76. 最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。
"""
"""
方式１　滑动窗口
"""
from collections import Counter


# 方式1
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1 = Counter(t)
        left = 0
        result = ""
        for index, val in enumerate(s):
            if val in d1:
                d1[val] -= 1
            # 包含t,右边确定为index
            if max(d1.values()) <= 0:
                # 判断左边界
                while True:
                    if s[left] in d1:
                        d1[s[left]] += 1
                        if d1[s[left]] == 1:
                            left += 1
                            break
                    left += 1
                # 判断结果是否为最短
                if not result:
                    result = s[left - 1:index + 1]
                else:
                    if len(result) > index - left + 2:
                        result = s[left - 1:index + 1]
        return result


if __name__ == '__main__':
    a = "ADOBECODEBANC"
    b = "ABC"
    s = Solution()
    print(s.minWindow(a, b))
