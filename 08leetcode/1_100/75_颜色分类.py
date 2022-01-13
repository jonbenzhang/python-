"""
75. 颜色分类
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
"""
"""
方式1 快排排序
方式2 归并排序
方式3 双指针
"""
from typing import List


# 方式１
class Solution:
    def part_index(self, nums, left, right):
        part = nums[left]
        mark = left
        for i in range(left + 1, right + 1):
            if nums[i] < part:
                mark += 1
                nums[mark], nums[i] = nums[i], nums[mark]
        nums[mark], nums[left] = nums[left], nums[mark]
        return mark

    def quick_sort(self, nums, left, right):
        if left >= right:
            return
        part = self.part_index(nums, left, right)
        self.quick_sort(nums, left, part - 1)
        self.quick_sort(nums, part + 1, right)

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.quick_sort(nums, 0, len(nums) - 1)


# 方式2_1
# 归并排序,新生成的,没有在原来的数组上修改，所以没过去
class Solution:

    def merge(self, nums_left, nums_right):
        i = 0
        j = 0
        merge_nums = []
        while i < len(nums_left) and j < len(nums_right):
            if nums_left[i] < nums_right[j]:
                merge_nums.append(nums_left[i])
                i += 1
            else:
                merge_nums.append(nums_right[j])
                j += 1
        if i < len(nums_left):
            for index in range(i, len(nums_left)):
                merge_nums.append(nums_left[index])
        if j < len(nums_right):
            for index in range(j, len(nums_right)):
                merge_nums.append(nums_right[index])
        return merge_nums

    def merge_sort(self, nums, left, right):
        if left == right:
            return [nums[left]]
        mid = left + right >> 1
        nums_left = self.merge_sort(nums, left, mid)
        nums_right = self.merge_sort(nums, mid + 1, right)
        # print(nums_left,nums_right)
        tmp = self.merge(nums_left, nums_right)
        print(tmp)
        return tmp

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = self.merge_sort(nums, 0, len(nums) - 1)
        return nums


# 方式2_2
class Solution:

    def merge(self, nums, left, mid, right):
        tmp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if nums[i] < nums[j]:
                tmp.append(nums[i])
                i += 1
            else:
                tmp.append(nums[j])
                j += 1
        for q in range(i, mid + 1):
            tmp.append(nums[q])
        for q in range(j, right + 1):
            tmp.append(nums[q])
        nums[left:right + 1] = tmp

    def merge_sort(self, nums, left, right):
        if left == right:
            return
        mid = left + right >> 1
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)
        return

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.merge_sort(nums, 0, len(nums) - 1)


# 方式3
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        point = 0
        while point <= right:
            if nums[point] == 0:
                nums[left], nums[point] = nums[point], nums[left]
                left += 1
                point += 1
            elif nums[point] == 2:
                nums[right], nums[point] = nums[point], nums[right]
                right -= 1
            else:
                point += 1


if __name__ == '__main__':
    a = [2, 0, 2, 1, 1, 0]
    s = Solution()
    print(s.sortColors(a))
