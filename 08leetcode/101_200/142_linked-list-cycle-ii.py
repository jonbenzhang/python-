"""
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

进阶：

你是否可以使用 O(1) 空间解决此题？

"""
"""
方式1,遍历然后通过hash存储每一个遍历过的节点
方式2  首先使用Floyd 判圈算法(龟兔赛跑算法),然后使用一个指针判断入环点位置
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head and head.next and head.next:
            slow_node = head
            fast_node = head
            pre_node = head
            pos = 0
        else:
            return None
        while fast_node and fast_node.next and fast_node.next.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if slow_node == fast_node:
                break
        if slow_node != fast_node:
            return None
        else:
            while pre_node != slow_node:
                pre_node = pre_node.next
                slow_node = slow_node.next
                pos += 1
            return pre_node
