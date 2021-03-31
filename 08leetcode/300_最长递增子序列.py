"""
300. 最长递增子序列
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
"""
"""
方式1 动态规划
"""
from typing import List

# 方式１
"""
状态转移方程
dp[i] = dp[j]+1(找到前面小于nums[i],的最大dp[j])
max(dp)
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            max_v = 0
            for j in range(1, i):
                if nums[j - 1] < nums[i - 1]:
                    max_v = max(max_v, dp[j])
            dp[i] = max_v + 1
        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))
    # print(s.lengthOfLIS([0, 1, 2, 3]))
