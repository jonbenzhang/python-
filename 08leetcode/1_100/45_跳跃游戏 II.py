"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
"""
"""
方式1 贪心算法
"""
from typing import List


# 方式1_1
# 从后往前跳,每次找到可以跳到的最远
class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        step_now = len(nums) - 1
        while step_now > 0:
            for i in range(step_now):
                if i + nums[i] >= step_now:
                    step_now = i
                    steps += 1
                    break
        return steps


# 方式1_2
# 从前往后跳,在当前节点可以跳到的所有节点中，选择可以跳到最远的节点
class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = 0
        max_pos, end, start = 0, 0, 0
        size = len(nums)
        for i in range(size - 1):
            max_pos = max(max_pos, i + nums[i])
            if i == end:
                steps += 1
                end = max_pos
                # 不判断的话也可以,只是优化
                if max_pos >= size - 1:
                    break
        return steps
