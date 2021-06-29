"""
31. 下一个排列
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。
"""
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                val = i
                for j in range(i + 1, len(nums)):
                    if nums[i - 1] < nums[j] < nums[i]:
                        val = j
                nums[i-1], nums[val] = nums[val], nums[i-1]
                nums[i:] = sorted(nums[i:])
                return
        nums.sort()
if __name__ == '__main__':
    a = [1,2,3]
    s = Solution()
    s.nextPermutation(a)
    print(a)