class item:
    def __init__(self, data):
        self.data = data
        self.next = None


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @classmethod
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
            if tail.val == 0 and head == tail:
                tail.val = sum % 10
            else:
                b = ListNode(sum % 10)
                tail.next = b
                tail = b
        return head


a = ListNode(2)
a2 = ListNode(4)
a3 = ListNode(3)
a.next = a2
# a2.next = a3

b = ListNode(5)
b2 = ListNode(6)
b3 = ListNode(4)
b.next = b2
b2.next = b3


print(Solution.addTwoNumbers(a, b).val)