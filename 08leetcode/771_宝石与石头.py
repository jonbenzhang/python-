"""
771. 宝石与石头
 给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。
"""


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        j_set = set(jewels)
        for i in stones:
            if i in j_set:
                count += 1
        return count
