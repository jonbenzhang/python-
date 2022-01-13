"""
86. 分隔链表
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。
你应当 保留 两个分区中每个节点的初始相对位置。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left = left_tmp = ListNode()
        right = right_tmp = ListNode()
        while head:
            if head.val < x:
                left_tmp.next = head
                left_tmp = left_tmp.next
            else:
                right_tmp.next = head
                right_tmp = right_tmp.next
            head = head.next
        right_tmp.next = None
        left_tmp.next = right.next
        return left.next
