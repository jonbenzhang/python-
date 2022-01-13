"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
"""

class Solution:
    @classmethod
    def threeSum(self, nums):
        # def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        results = []
        for i in range(len(nums) - 2):
            # 如果最小的都大于0,肯定三数之和大于0
            if nums[i] > 0:
                return results
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j, k = i + 1, len(nums) - 1
            # 等价于查找所有符合条件的两个数
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
        return results


if __name__ == '__main__':
    Solution.threeSum([-1, 0, 1, 2, -1, -4])
