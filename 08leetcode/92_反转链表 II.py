"""
92. 反转链表 II
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return None
        result = tmp = ListNode(0, head)
        a, b = None, None
        for i in range(right + 2):
            if i == left - 1:
                a = tmp
            if i == right + 1:
                b = tmp
                break
            tmp = tmp.next
        cur = b
        pre = a.next
        while pre != b:
            t = pre.next
            pre.next = cur
            cur = pre
            pre = t
        a.next = cur
        return result.next


