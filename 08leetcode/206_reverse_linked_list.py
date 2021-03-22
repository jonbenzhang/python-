"""
206. 反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""
"""
方式1,新开一个链表
方式2 双指针
方式3 递归
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方式1
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        tmp = head
        l2 = None
        while tmp:
            d = ListNode(tmp.val)
            d.next = l2
            l2 = d
            tmp = tmp.next
        return l2


# 方式2
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = None
        pre = head
        while pre:
            t = pre.next
            pre.next = cur
            cur = pre
            pre = t
        return cur


# 方式3
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 递归终止条件是当前为空，或者下一个节点为空
        if (head == None or head.next == None):
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList(head.next)
        # 这里请配合动画演示理解
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        # 没有这一个,倒数第一个节点和倒数第二个的节点的循环,倒数第一个节点的next指向倒数第二个,而不是指向None
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur
