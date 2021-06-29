"""
87. 扰乱字符串
使用下面描述的算法可以扰乱字符串 s 得到字符串 t ：
如果字符串的长度为 1 ，算法停止
如果字符串的长度 > 1 ，执行下述步骤：
在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 s ，则可以将其分成两个子字符串 x 和 y ，且满足 s = x + y 。
随机 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即，在执行这一步骤之后，s 可能是 s = x + y 或者 s = y + x 。
在 x 和 y 这两个子字符串上继续从步骤 1 开始递归执行此算法。
给你两个 长度相等 的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。如果是，返回 true ；否则，返回 false 。
"""
"""
方式1 暴力递归,时间过长
方式2 递归
方式3 动态规划
"""
import functools
from collections import Counter


# 方式1暴力递归
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # @functools.lru_cache(None)
        def dfs(array):
            print(array)
            if "".join(array) == s2:
                return True
            if len(array) == len(s1):
                return False
            for i in range(len(array)):
                if len(array[i]) >= 2:
                    for j in range(1, len(array[i])):
                        if dfs(array[0:i] + [array[i][0:j], array[i][j:]] + array[i + 1:]) or dfs(array[0:i] + [array[i][j:], array[i][0:j]] + array[i + 1:]):
                            return True
            return False

        return dfs([s1])

# 方式2
class Solution:
    @functools.lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2) or Counter(s1) != Counter(s2):
            return False
        for i in range(1,len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:],s2[:-i]):
                return True
        return False

# 方式3
class Solution:
    @functools.lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        
        return False
if __name__ == '__main__':
    a = "abcda"
    b = "aabdc"
    s = Solution()
    print(s.isScramble(a, b))
