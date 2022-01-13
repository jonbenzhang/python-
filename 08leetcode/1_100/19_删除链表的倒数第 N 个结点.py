"""
19. 删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
进阶：你能尝试使用一趟扫描实现吗？
"""
"""
方式1 双指针
方式2 使用栈，倒数第n个弹出的就是要删除的
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方式1
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        a = ListNode()
        a.next = head
        left, right = a, a
        for _ in range(n + 1):
            right = right.next
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next
        return a.next
