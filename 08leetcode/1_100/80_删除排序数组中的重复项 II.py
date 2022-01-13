"""
80. 删除排序数组中的重复项 II
给定一个增序排列数组 nums ，你需要在 原地 删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
"""
"""
方式１　暴力删除
方式2 双指针
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) - 3, -1, -1):
            if nums[i] == nums[i + 2]:
                del nums[i + 2]
        return len(nums)


# 方式2
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 2, 2
        while j < len(nums):
            if nums[i - 2] != nums[j]:
                nums[i] = nums[j]
                i += 1
            j += 1

        return i
