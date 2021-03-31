"""
81. 搜索旋转排序数组 II
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        nums_len = right
        while left <= right:
            mid = left + right >> 1
            if target == nums[mid]:
                return True
            if nums[0] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[nums_len]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                while left < nums_len and nums[left] == nums[mid]:
                    left += 1
                while right >= 0 and nums[right] == nums[mid]:
                    right -= 1
        return False


if __name__ == '__main__':
    a = [1, 0, 1, 1, 1, ]
    s = Solution()
    print(s.search(a, 0))
