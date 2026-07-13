# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = None
        tail1, tail2 = l1, l2
        while tail1 and tail2:
            if carry != 0:
                tail1.val += carry
                carry = 0

            val = tail1.val + tail2.val
            remainder = val % 10
            carry = val // 10
            
            tail1.val = remainder
            prev = tail1
            tail1 = tail1.next
            tail2 = tail2.next
        if tail2:
            prev.next = tail2
            tail1 = prev.next
        while carry != 0:
            if not tail1:
                prev.next = ListNode()
                tail1 = prev.next
                val = carry
            else:
                val = tail1.val + carry
            remainder = val % 10
            carry = val // 10
            tail1.val = remainder
            prev = tail1
            tail1 = tail1.next
        return l1
