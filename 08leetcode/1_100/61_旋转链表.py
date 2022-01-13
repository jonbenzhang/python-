"""
61. 旋转链表
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。
"""
"""
方式1 两次遍历
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方式1
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        start = tmp = head
        count = 1
        while tmp.next:
            tmp = tmp.next
            count += 1
        tmp.next = head
        for _ in range(count - (k % count) - 1):
            start = start.next
        result = start.next
        start.next = None
        return result
