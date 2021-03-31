"""
18. 四数之和
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
注意：答案中不可以包含重复的四元组。
"""
from typing import List

"""
方式1 排序加双指针
"""


# 方式1
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] * 4 > target:
                return results
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] * 3 > target:
                    break
                target2 = target - nums[i] - nums[j]
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if left > j + 1 and nums[left] == nums[left - 1]:
                        left += 1
                        continue
                    if right < len(nums) - 1 and nums[right] == nums[right + 1]:
                        right -= 1
                        continue
                    if nums[left] + nums[right] == target2:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] < target2:
                        left += 1
                    else:
                        right -= 1
        return results


if __name__ == '__main__':
    a = [-2, -1, -1, 1, 1, 2, 2]
    b = 0
    s = Solution()
    print(s.fourSum(a, b))
