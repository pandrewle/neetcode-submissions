import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        i = 0
        for x,y in points:
            dist = -math.hypot(x,y)
            heapq.heappush(maxheap, (dist, (x,y)))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        return [coord for dist, coord in maxheap]
        