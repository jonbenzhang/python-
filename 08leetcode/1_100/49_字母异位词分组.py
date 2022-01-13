"""
49. 字母异位词分组
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。
"""
"""
方式１　字符串排序
方式2   统计字符串中每个字母出现的次数
"""
from typing import List

from collections import defaultdict

"""
方式1
对每一个字符串进行排序，用排序后的字符串作为key值
使用有默认值的字典，就不用每次判断是否已经创建了该key值，和对应的val
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for str in strs:
            str_s = "".join(sorted(str))
            d[str_s].append(str)
        return list(d.values())


"""
方式2 统计每一个字母出现的次数

可变类型是不可以进行哈希的,所以把列表转成元组
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for str in strs:
            # 统计对应的26个字母,每一个出现的次数
            count = [0] * 26
            for i in str:
                # 计算该字母对应的下标并进行加一
                count[ord(i) - ord('a')] += 1
            # 可变类型是不可以进行哈希的,所以把列表转成元组
            d[tuple(count)].append(str)
        return list(d.values())
