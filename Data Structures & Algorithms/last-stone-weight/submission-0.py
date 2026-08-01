import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for stone in stones:
            heapq.heappush(maxheap, -stone)
        while len(maxheap) > 1:
            x, y = -heapq.heappop(maxheap), -heapq.heappop(maxheap)
            if x > y:
                heapq.heappush(maxheap, -(x-y))
        return -maxheap[0] if maxheap else 0
