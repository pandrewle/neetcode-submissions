import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pairs = [(-math.hypot(x,y), (x,y)) for x,y in points]
        maxheap = []
        heapq.heapify(maxheap)
        i = 0
        while i < len(pairs):
            heapq.heappush(maxheap, pairs[i])
            if len(maxheap) > k:
                heapq.heappop(maxheap)
            i += 1
        return [coord for dist, coord in maxheap]
        