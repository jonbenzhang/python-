"""
55. 跳跃游戏
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个下标。
"""
"""
方式1 贪心算法 Greedy
"""
from typing import List


# 方式1_1
class Solution:
    @classmethod
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0
        size = len(nums)
        for i in range(size):
            if i <= max_index:
                max_index = max(nums[i] + i, max_index)
            else:
                return False
        return True


# 方式1_2
# 从后往前推
class Solution:
    @classmethod
    def canJump(self, nums: List[int]) -> bool:
        j = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if j - i <= nums[i]:
                j = i
        if j == 0:
            return True
        else:
            return False


# 方式1_1

if __name__ == '__main__':
    print(Solution.canJump([1, 2, 3]))
