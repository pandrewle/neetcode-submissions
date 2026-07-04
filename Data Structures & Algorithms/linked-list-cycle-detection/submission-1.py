# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 0
        curr = head
        while curr:
            if curr.val == float('inf'):
                return True
            curr.val = float('inf')
            curr = curr.next
        return False