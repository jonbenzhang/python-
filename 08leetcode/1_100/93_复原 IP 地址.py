"""
93. 复原 IP 地址
给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。
例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
"""
"""
方式１　dfs
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []

        def dfs(level, start, result):
            if level == 4:
                if start == len(s):
                    results.append(result)
                return
            if start + 1 <= len(s):
                dfs(level + 1, start + 1, result + [s[start]])
            if not s[start:start + 2].startswith('0') and start + 2 <= len(s):
                dfs(level + 1, start + 2, result + [s[start:start + 2]])
            if not s[start:start + 3].startswith('0') and start + 3 <= len(s) and int(s[start:start + 3]) <= 255:
                dfs(level + 1, start + 3, result + [s[start:start + 3]])

        dfs(0, 0, [])
        return [".".join(i) for i in results]


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("1111"))
