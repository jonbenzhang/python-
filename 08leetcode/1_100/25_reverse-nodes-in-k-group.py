""""
25. K 个一组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
进阶：
你可以设计一个只使用常数额外空间的算法来解决此问题吗？
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""
"""
1.方式1 普通交换
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 方式1
class Solution:
    def reverseList(self, head: ListNode, k):
        """
        列表reverse
        :param head:
        :return:
        """
        cur = None
        pre = head
        while pre and k:
            t = pre.next
            pre.next = cur
            cur = pre
            pre = t
            k -= 1
        return cur, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        l1 = ListNode()
        l1.next = head
        l2 = l1
        while l2.next:
            sign = True
            l2_head = l2.next
            l2_end = l2.next
            for _ in range(k):
                if l2_end:
                    l2_end = l2_end.next
                else:
                    sign = False
                    break
            if sign:
                cur, end = self.reverseList(l2_head, k)
                l2.next = cur
                end.next = l2_end
                l2 = end
            else:
                break

        return l1.next
