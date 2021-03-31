"""
41. 缺失的第一个正数
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
进阶：你可以实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案吗？
"""
"""
方式1 使用set保存已经有的正数,然后正数从１开始遍历
方式2 置换
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_len = len(nums)
        for i in range(nums_len):
            while nums[i] not in [0, i + 1]:
                if nums[i] <= 0 or nums[i] > nums_len:
                    nums[i] = 0
                else:
                    val = nums[i]
                    if nums[val - 1] == val:
                        nums[i] = 0
                        continue
                    nums[i], nums[val - 1] = nums[val - 1], val
        for i in range(nums_len):
            if nums[i] != i + 1:
                return i + 1
        return nums_len + 1


if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive([1, 1]))
