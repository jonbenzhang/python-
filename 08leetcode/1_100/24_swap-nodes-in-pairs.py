"""
24. 两两交换链表中的节点
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
"""
"""
方式1,普通交换
方式2 递归
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方式1
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        l1 = ListNode()
        l1.next = head
        l2 = l1
        while l2.next and l2.next.next:
            tmp = l2.next.next
            # 前一个点指向后一个点的next
            l2.next.next = l2.next.next.next
            tmp.next = l2.next
            l2.next = tmp
            l2 = l2.next.next
        return l1.next


# 方式2
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        ret = self.swapPairs(head.next.next)
        tmp = head.next
        head.next = ret
        tmp.next = head
        return tmp

