# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseGroup(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        tail = head
        while tail:
            tempNode = tail.next
            tail.next = prev
            prev = tail
            tail = tempNode
        return prev

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 1
        dummy = ListNode(0, head)
        group_head, tail, prev_group_tail = head, head, dummy
        while tail:
            if count == k:
                next_group_start = tail.next
                tail.next = None
                reverse_head = self.reverseGroup(group_head)

                prev_group_tail.next = reverse_head
                group_head.next = tail = next_group_start

                prev_group_tail = group_head
                group_head = next_group_start
                count = 1                
            else:
                tail = tail.next
                count += 1

        return dummy.next
