"""
23. 合并K个升序链表
给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。
"""
"""
方式1 使用小顶堆
方式2 分治
"""
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List


# 方式１
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode()
        tmp = head
        q = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(q, [lists[i].val, i])
                lists[i] = lists[i].next
        while q:
            val, i = heapq.heappop(q)
            tmp.next = ListNode(val)
            tmp = tmp.next
            if lists[i]:
                heapq.heappush(q, [lists[i].val, i])
                lists[i] = lists[i].next
        return head.next


# 方式2 分治
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        return self.merge(lists, 0, len(lists) - 1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + right >> 1
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid + 1, right)
        return self.mergeTwoLists(l1, l2)
