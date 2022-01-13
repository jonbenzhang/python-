# 暴力法
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 方式1
        # 两层循环的方法,类似于冒泡
        # for j in range(len(nums)):
        #     for i in range(len(nums)-j-1):
        #         if nums[i]==0 and nums[i+1]!=0:
        #             nums[i],nums[i+1] = nums[i+1],nums[i]
        # return nums
        # 方式2
        # 一层loop
        j = 0
        for i in range(len(nums)):

            if nums[i] != 0:
                if i != j:
                    nums[j] = nums[i]
                    nums[i] = 0
                j += 1
        return nums
        ## 方式3
        # 进行交换
        j = 0
        for i in range(len(nums)):

            if nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums


"""
方式2,和方式3,都是使用双指针的方法,
前面一个指向已经处理好的数据的尾部，另一个执行正在处理的数据
"""
