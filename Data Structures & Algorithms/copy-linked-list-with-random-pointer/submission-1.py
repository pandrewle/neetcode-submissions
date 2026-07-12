"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copy = {}
        tail = head
        prev = tail
        count = 0
        while tail:
            copy[tail] = Node(tail.val, tail.next, tail.random)
            if prev:
                copy[prev].next = copy[tail]
            prev = tail
            tail = tail.next
            count += 1
        copy[prev].next = None
        newHead = copy[head]
        tail = copy[head]
        while tail:
            if tail.random:
                tail.random = copy[tail.random]
            else:
                tail.random = None
            tail = tail.next
        return newHead

            