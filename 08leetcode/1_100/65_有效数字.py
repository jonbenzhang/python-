"""
65. 有效数字
有效数字（按顺序）可以分成以下几个部分：
一个 小数 或者 整数
（可选）一个 'e' 或 'E' ，后面跟着一个 整数
小数（按顺序）可以分成以下几个部分：
（可选）一个符号字符（'+' 或 '-'）
下述格式之一：
至少一位数字，后面跟着一个点 '.'
至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
一个点 '.' ，后面跟着至少一位数字
整数（按顺序）可以分成以下几个部分：
（可选）一个符号字符（'+' 或 '-'）
至少一位数字
部分有效数字列举如下：
["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
部分无效数字列举如下：
["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。
"""
"""
方式1 自定义匹配法
方式2　有dfh的方法,没哟仔细看
"""
# 方式1
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()
        l = s.split("e")
        numbers = {str(i) for i in range(10)}
        if len(l) > 2:
            return False
        if len(l) == 2:
            if not len(l[0]) or not len(l[1]):
                return False
            if l[1][0] in ['+', '-']:
                l[1] = l[1][1:]
                if not l[1]:
                    return False
            for i in l[1]:
                if i not in numbers:
                    return False
        if l[0][0] in ['+', '-']:
            l[0] = l[0][1:]
            if not l[0]:
                return False
        if l[0].count('.') > 1 or l[0] == '.':
            return False
        for i in l[0]:
            if i not in {'.'} | numbers:
                return False
        return True
