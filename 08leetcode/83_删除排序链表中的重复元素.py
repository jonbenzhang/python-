"""
83. 删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
"""
"""
方式1 双指针
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        f = head.val
        pre = head
        tmp = head.next
        while tmp:
            if tmp.val == f:
                pre.next = tmp.next
                tmp = pre.next
            else:
                f = tmp.val
                tmp = tmp.next
                pre = pre.next
        return head
