# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tail = head
        length = 0
        while tail:
            length += 1
            tail = tail.next
        tail, prev = head, head
        count = 0
        while tail:
            print(f'length {length}')
            print(f'count {count}')
            if count == (length - n) and (length-n) == 0:
                print('here 1!')
                head = tail.next
                return head
            elif count == (length - n) and (length-n) != 0:
                prev.next = tail.next
                return head
            else:
                prev = tail
                tail = tail.next
                count += 1
        return head


