import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pairs = [(-math.hypot(x,y), (x,y)) for x,y in points]
        heapq.heapify(pairs)
        while len(pairs) > k:
            heapq.heappop(pairs)
        return [coord for dist, coord in pairs]
        