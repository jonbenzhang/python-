"""
153. 寻找旋转排序数组中的最小值
假设按照升序排序的数组在预先未知的某个点上进行了旋转。例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] 。

请找出其中最小的元素。

nums 中的所有整数都是 唯一 的
"""
from typing import List

"""
方式1 二分法
"""


# 方式1_1
# 找到最大值，然后最大值的下一个就是最小值
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right + 1) // 2
            if nums[0] < nums[mid]:
                left = mid
            else:
                right = mid - 1
        # print(left,right)
        return nums[(left + 1) % len(nums)]


# 方式1_2

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            print(left, right)
            mid = (left + right) // 2
            # 这个位置小于和小于等于都可以
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid + 1
        return nums[right]
