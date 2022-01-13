"""
239. 滑动窗口最大值
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
返回滑动窗口中的最大值。
"""
"""
方式1,暴力方法简单方法
方式2,单调队列,双向队列
方式3,使用大根堆
"""
from typing import List


# 方式1,无法通过时间过长
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = k - 1
        l = []
        while right < len(nums):
            l.append(max(nums[left:right + 1]))
            left += 1
            right += 1
        return l


import collections


# 方式2，（下面的方法错误，下面的方式2是正确的）
# 单调队列,双向队列
# 从小到大的单调队列会造成，到i时,nums[i]小于队列中的最大元素，然后把nums[i]丢弃掉了．
# 然而nums[i]是后面的某一滑动窗口的最大元素，造成程序错误
class Solution:
    @classmethod
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        size = len(nums)
        # 先把第一个窗口中的前k个数据，判断放入单调队列
        for i in range(k):
            if not q or nums[i] > nums[q[-1]]:
                q.append(i)
        res.append(nums[q[-1]])
        for i in range(k, size):
            if q and q[0] <= i - k:
                q.popleft()
            if not q or nums[i] > nums[q[-1]]:
                q.append(i)
            res.append(nums[q[-1]])
        return res


# 方式2
# 单调队列从大到小
class Solution:
    @classmethod
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque()
        size = len(nums)
        # 先把第一个窗口中的前k个数据，判断放入单调队列
        for i in range(k):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        for i in range(k, size):
            if q and q[0] <= i - k:
                q.popleft()
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            res.append(nums[q[0]])
        return res


if __name__ == '__main__':
    print(Solution.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))
