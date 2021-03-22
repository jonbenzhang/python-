"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

"""
"""
1.方式1,枚举
2.方式2,使用list.index()
3.方式3 使用字典

"""


# 方式1
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# 方式2
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        index2 = 0
        for i in range(len(nums) - 1):
            j = target - nums[i]
            try:
                index2 = nums.index(j, i + 1)  # 从i+1开始寻找
            except:
                index2 = 0
            if index2:
                return [i, index2]


# 方式3
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i in range(len(nums)):
            index1 = d.get(nums[i])
            if index1 is not None:
                return [index1, i]
            else:
                d[target - nums[i]] = i
