"""
189. 旋转数组
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

进阶：
尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
"""
"""
1.方式1 每次整体移动一个位置，移动k次
2.方式2 记录后k个元素,然后通过对索引相差k的元素进行移动
3.方式3 多次反转
"""


# 方式1
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for _ in range(k):
            d = nums[-1]
            for i in range(len(nums)):
                nums[i], d = d, nums[i]


# 方式2
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums2 = nums[-k:]
        for j in range(k):
            d = nums2[j-k]
            for i in range(0, len(nums), k):
                nums[i], d = d, nums[i]

