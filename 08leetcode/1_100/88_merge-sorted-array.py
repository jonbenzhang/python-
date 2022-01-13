"""
88. 合并两个有序数组
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。
"""
import sys


class Solution:
    @classmethod
    # def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    def merge(self, nums1, m, nums2, n) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, k = m - 1, m + n - 1
        j = n - 1
        while i >= 0 or j >= 0:
            if i == -1:
                nums1[:k+1] = nums2[:j+1]
                break
            if j == -1:
                break
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        print(nums1)


if __name__ == '__main__':
    # Solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    Solution.merge([0], 0, [1], 1)
