"""
34. 在排序数组中查找元素的第一个和最后一个位置
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
"""
"""
方式1 暴力匹配
方式2 二分法
"""
from typing import List


# 方式2
class Solution:
    def binary_search_left(self, nums, target):
        """
        确定左边界
        :param nums:
        :param target:
        :return:
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + right >> 1
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return min(left, len(nums) - 1)

    def binary_search_right(self, nums, target):
        """
        确定右边界
        :param nums:
        :param target:
        :return:
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + right >> 1
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = self.binary_search_left(nums, target)
        if nums[left] != target:
            return [-1, -1]
        right = self.binary_search_right(nums, target)
        return [left, right]


if __name__ == '__main__':
    a = [5, 7, 7, 8, 8, 10]
    b = 8
    s = Solution()
    print(s.searchRange(a, b))
