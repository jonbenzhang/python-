"""
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
"""
"""
方式1,两个字符串进行排序
方式2,每个字母存储进行哈希,比对
"""


# 方式1，python中字符字符串没有直接排序方法,所以转成列表后进行排序
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_l = list(s)
        t_l = list(t)
        s_l.sort()
        t_l.sort()
        s1 = "".join(s_l)
        t1 = "".join(t_l)
        if s1 == t1:
            return True
        else:
            return False


# 方式2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_d = {}
        for i in s:
            if i not in s_d:
                s_d[i] = 0
            s_d[i] += 1
        for i in t:
            if i not in s_d:
                return False
            s_d[i] -= 1
            if s_d[i] < 0:
                return False
        if sum(s_d.values())!=0:
            return False
        return True
