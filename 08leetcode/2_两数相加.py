"""
2. 两数相加
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
"""

"""
方式１ 模拟现实情况
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 方式1
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        tail = head
        carry = 0
        while l1 or l2 or carry:
            sum = (0 if not l1 else l1.val) + (0 if not l2 else l2.val) + carry
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            carry = int(sum / 10)
            b = ListNode(sum % 10)
            tail.next = b
            tail = b
        return head.next
