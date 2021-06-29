"""
82. 删除排序链表中的重复元素 II
存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除链表中所有存在数字重复情况的节点，只保留原始链表中 没有重复出现 的数字。
返回同样按升序排列的结果链表。
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
        tmp = ListNode(0,head)
        result = tmp
        sign = False
        while tmp and tmp.next and tmp.next.next:
            while tmp.next and tmp.next.next and tmp.next.val == tmp.next.next.val:
                sign = True
                tmp.next = tmp.next.next.next
            if sign:
                tmp.next = tmp.next.next
                sign = False
            else:
                tmp = tmp.next
        return result.next


