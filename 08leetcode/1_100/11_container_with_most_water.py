"""
11. 盛最多水的容器
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。
"""
"""
1.方式1就是暴力求解,枚举 O(n^2)
双层循环得到最大的值,
2.方式2,左右夹逼
从两边向里靠近,每次向里面挪动高度小的棒子


"""


# 方式1
class Solution:
    def maxArea(self, height: list[int]) -> int:
        # 双层循环
        max_val = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                max_val = max((min(height[i], height[j]) * (j - i)), max_val)
        return max_val


# 方式2
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_val = 0
        i, j = 0, len(height) - 1
        while i < j:
            max_val = max((min(height[i], height[j]) * (j - i)), max_val)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return max_val


# 方式3

if __name__ == '__main__':
    for i in range(5):
        i += 2
        print(i)
